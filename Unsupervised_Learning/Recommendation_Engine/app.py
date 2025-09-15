from flask import Flask, render_template, request
import pandas as pd
from sqlalchemy import create_engine
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from urllib.parse import quote_plus

# Flask app initialization
app = Flask(__name__)

# Database connection - update with your credentials
user = 'root'
pw = 'root'
db = 'Recommendation_engine'
pw = quote_plus(pw)
engine = create_engine(f'mysql+pymysql://{user}:{pw}@localhost/{db}')

# Read game data from DB
sql = 'SELECT * FROM game_table;'
df = pd.read_sql(sql, engine)

# Prepare user-item rating matrix
user_rating_game = df.pivot_table(index='userId', columns='game', values='rating').fillna(0)
cosine_user = cosine_similarity(user_rating_game)
cosine_user_df = pd.DataFrame(cosine_user, index=user_rating_game.index, columns=user_rating_game.index)

# Prepare content-based similarity
df_unique = df.drop_duplicates(subset='game').reset_index(drop=True)
vectorizer = TfidfVectorizer(stop_words='english')
tfid_game = vectorizer.fit_transform(df_unique['game'])
cosine_game = cosine_similarity(tfid_game)
indices = pd.Series(df_unique.index, index=df_unique['game']).drop_duplicates()

def recommend_game(userid, game_name, topN=5, alpha=0.9, topK=5):
    if userid not in user_rating_game.index:
        return pd.DataFrame()
    if game_name not in indices:
        return pd.DataFrame()

    similar_user = cosine_user_df[userid].drop(labels=[userid]).sort_values(ascending=False).head(topK)
    weighted_ratings = user_rating_game.loc[similar_user.index].T.dot(similar_user) / similar_user.sum()

    rated_games = df[df['userId'] == userid]['game'].tolist()
    weighted_ratings = weighted_ratings.drop(labels=rated_games, errors='ignore')

    idx = indices[game_name]
    sim_scores = list(enumerate(cosine_game[idx].flatten()))
    sim_scores = [t for t in sim_scores if t[0] != idx]
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[:topN + 1]
    content_games = [df_unique.loc[i, 'game'] for i, score in sim_scores if i in df_unique.index]
    content_scores = pd.Series([score for i, score in sim_scores if i in df_unique.index], index=content_games)

    content_scores = content_scores.drop(labels=rated_games, errors='ignore')

    common_games = weighted_ratings.index.intersection(content_scores.index)
    final_user_scores = weighted_ratings[common_games].fillna(0)
    final_content_scores = content_scores[common_games].fillna(0)
    final_score = alpha * final_user_scores + (1 - alpha) * final_content_scores

    remaining_content = content_scores.drop(labels=common_games, errors='ignore').fillna(0)
    final_score = pd.concat([final_score, (1 - alpha) * remaining_content])

    final_score = final_score.sort_values(ascending=False).head(topN)
    return final_score.reset_index().rename(columns={'index': 'Recommended Games', 0: 'Score'})

@app.route('/')
def home():
    games_list = df_unique['game'].tolist()
    users_list = user_rating_game.index.tolist()
    return render_template('index.html', games_list=games_list, users_list=users_list)

@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        userid = int(request.form['userid'])
        game_name = request.form['game_name']
        top_n = int(request.form['topn'])
        recommendations = recommend_game(userid, game_name, topN=top_n)
        if recommendations.empty:
            message = "No recommendations found for the input."
            return render_template('data.html', message=message, table='')
        recommendations.to_sql('top_10', con=engine, if_exists='replace', index=False)
        html_table = recommendations.to_html(classes='table table-striped', index=False)
        return render_template('data.html', message="Recommendations saved to database", table=html_table)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

