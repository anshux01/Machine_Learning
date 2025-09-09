# Unsupervised Learning: KMeans & DBSCAN Clustering

## Project Overview
This project focuses on **unsupervised learning** techniques to analyze **airline passenger traffic data** and identify meaningful clusters. It uses **KMeans**, **DBSCAN**, and **Hierarchical Clustering** to uncover patterns in passenger counts, terminal usage, and airline operations.

The goal is to provide actionable insights for **airport operations, marketing, and resource optimization**.

---

## Dataset
The dataset used in this project contains **airline passenger statistics** with the following key fields:

| Field                     | Description                                  |
|----------------------------|----------------------------------------------|
| Activity Period           | Year-Month identifier (YYYYMM)               |
| Operating Airline          | Name of the airline                           |
| Operating Airline IATA Code| Two-character airline code                    |
| GEO Region                 | Geographic region of operation               |
| Terminal                   | Airport Terminal                              |
| Boarding Area              | Boarding Gate/Area                             |
| Passenger Count            | Number of passengers                           |
| Year                       | Year of operation                              |
| Month                      | Month of operation                             |

- Dataset size: **14,975 unique rows** (after cleaning)
- Source: Local CSV file or MySQL database

---

## Project Workflow

1. **Exploratory Data Analysis (EDA)**  
   - Checked distribution, skewness, and kurtosis of passenger counts  
   - Visualized categorical features and trends across years and months  

2. **Data Preprocessing**  
   - Handled missing values (`Operating Airline IATA Code`)  
   - Removed duplicates  
   - Outlier treatment using **Winsorization**  
   - Scaling numeric features using **MinMaxScaler**  
   - Encoding categorical features using **OneHotEncoder**

3. **Model Building**  
   - **KMeans Clustering**: Determined optimal `K` using silhouette score and elbow/knee method  
   - **DBSCAN**: Tuned `eps` and `min_samples` parameters  
   - **Hierarchical Clustering**: Visualized dendrograms and evaluated performance

4. **Evaluation**  
   - Silhouette scores used to compare clustering performance  
   - KMeans achieved the highest silhouette score: **~0.85**

---

## Files

| File Name                   | Description |
|------------------------------|-------------|
| `KMeans_DBSCAN_Clustering.ipynb` | Jupyter notebook with full analysis and clustering |
| `preprocessor.joblib`         | Saved preprocessing pipeline |
| `kmeans_model.joblib`         | Trained KMeans model |
| `dbscan_model.joblib`         | Trained DBSCAN model |
| `requirements.txt`            | Python dependencies for the project |
| Dataset CSV                  | `AirTraffic_Passenger_Statistics.csv` |

---

## Installation & Setup

1. Clone the repository:

```git clone https://github.com/anshux01/Machine_Learning.git```
```cd Machine_Learning/Unsupervised_Learning/K_Means_ans_DBscan```

2. Create a virtual environment (optional but recommended):

```python -m venv venv```
```source venv/bin/activate   # Linux / Mac```
```venv\Scripts\activate      # Windows```


3. Install dependencies:

```pip install -r requirements.txt```


4. Run the notebook:

```jupyter notebook KMeans_DBSCAN_Clustering.ipynb```

----

# Flask App Demo

1. Ensure the preprocessor.joblib and kmeans_model.joblib files are in the same directory as app.py.

2. Run the Flask app:

```python app.py```


3. Open a web browser and go to:

```http://127.0.0.1:5000```


4. You can interact with the app to:

- Upload new passenger data

- See clustering predictions

- Visualize cluster assignments

> Note: The app uses the trained KMeans model and preprocessing pipeline to predict clusters for new input data.

----

## Screenshots / Demo

- <img width="1612" height="960" alt="Screenshot 2025-09-09 150024" src="https://github.com/user-attachments/assets/5a4fc35f-9319-4292-8c6b-dd0884c1e3f6" />
- <img width="918" height="782" alt="Screenshot 2025-08-30 095426" src="https://github.com/user-attachments/assets/af8f2f12-8eb9-4c4d-b75a-8e143a619e9a" />

- <img width="1565" height="1042" alt="Screenshot 2025-09-09 150041" src="https://github.com/user-attachments/assets/8ec7c601-5c26-45bc-abe6-02083a4956e5" />

- <img width="1458" height="818" alt="Screenshot 2025-09-09 150210" src="https://github.com/user-attachments/assets/ed0ce765-ae6f-47da-8e37-3acf773c00a1" />
- <img width="1920" height="1080" alt="Screenshot 2025-09-09 095640" src="https://github.com/user-attachments/assets/4a20a693-5ef0-42af-b2f2-e64c6a387a3b" />
- <img width="1061" height="845" alt="Screenshot 2025-09-09 095538" src="https://github.com/user-attachments/assets/6b8e49db-40b2-4e3b-b58d-85fd1dd4c68e" />


-----
**Requirements**


```text
pandas
numpy
matplotlib
seaborn
scipy
scikit-learn
kneed
joblib
feature-engine
sqlalchemy
pymysql
flask
```

---
Key Insights

Airline passenger data is highly skewed and contains extreme outliers.

KMeans provided the best clustering results with clear cluster separation.

DBSCAN detected noise points but struggled with high variance in density.

Clustering can be used to optimize operations, marketing campaigns, and resource allocation.

-----
Author

Anshuman Acharya

LinkedIn: [Anshuman A Acharya](https://www.linkedin.com/posts/anshuman-a-acharya_datascience-machinelearning-clustering-activity-7371113974584537088-89L4?utm_source=share&utm_medium=member_desktop&rcm=ACoAAENnC2sBcZrn31mFIUf41h08wp3-w3f9PlQ)

GitHub: [anshux01](https://github.com/anshux01/Machine_Learning/tree/main/Unsupervised_Learning/K_Means_and_DBscan)


