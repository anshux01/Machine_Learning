from flask import render_template, request, Flask
import pandas as pd
import joblib
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Load preprocessing pipeline
preprocessor = joblib.load('preprocessor.joblib')

#Load Model
kmeans_model = joblib.load(open('kmeans_model.joblib','rb'))
dbscan_model = joblib.load(open('dbscan_model.joblib','rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        user = request.form['user']
        pw = quote_plus(request.form['pw'])
        db = request.form['db']

        #creating MySQ engine
        engine = create_engine(f'mysql+pymysql://{user}:{pw}@localhost/{db}')

        try:
            df = pd.read_csv(f)
        except:
            try:
                df = pd.read_excel(f)
            except:
                df = pd.DataFrame(f)

        clean_df =df.drop(["Operating Airline IATA Code","Operating Airline","Activity Period","Year","Month"], axis = 1) # Drop the unneeded columns

        data_preprocess = pd.DataFrame(preprocessor.transform(clean_df),columns=preprocessor.get_feature_names_out())

         # Predictions
        df["KMeans_Cluster"] = kmeans_model.predict(data_preprocess)
        df["DBSCAN_Cluster"] = dbscan_model.fit_predict(data_preprocess)

        # Save results in MySQL
        df.to_sql("airline_clusters", con=engine, if_exists="append", chunksize=1000, index=False)

        # Convert to HTML table
        html_table = df.head(50).to_html(classes="table table-striped", index=False)

        # Cluster summary
        kmeans_summary = df["KMeans_Cluster"].value_counts().to_frame().reset_index()
        kmeans_summary.columns = ["Cluster", "Count"]

        dbscan_summary = df["DBSCAN_Cluster"].value_counts().to_frame().reset_index()
        dbscan_summary.columns = ["Cluster", "Count"]

        kmeans_html = kmeans_summary.to_html(classes="table table-bordered", index=False)
        dbscan_html = dbscan_summary.to_html(classes="table table-bordered", index=False)

        # Render results
        return render_template(
            "data.html",
            Y=f"""
                <h2 style="text-align:center;">Clustered Passenger Data (Sample)</h2>
                {html_table}
                <hr>
                <h2 style="text-align:center;">KMeans Cluster Distribution</h2>
                {kmeans_html}
                <hr>
                <h2 style="text-align:center;">DBSCAN Cluster Distribution</h2>
                {dbscan_html}
            """
        )

# Run app
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)