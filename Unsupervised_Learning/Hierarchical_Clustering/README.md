# Hierarchical Clustering on Airline Passenger Data ✈️

## 📖 Overview
This project applies **Hierarchical Clustering** on airline passenger data to identify operational patterns, segment airlines/terminals, and provide insights for optimizing efficiency and financial health.  
The project follows the **CRISP-ML(Q)** methodology, ensuring structured delivery from business understanding to deployment.

## 🎯 Objectives
- Segment airlines and terminals using **hierarchical clustering**.
- Improve airline operational efficiency by **10–12%**.
- Achieve a **Silhouette Score ≥ 0.7** as ML success criteria.
- Provide actionable insights for **revenue growth** and **resource optimization**.

## 🛠️ Tech Stack
- **Python**: pandas, numpy, seaborn, matplotlib, scikit-learn, feature-engine  
- **SQL**: MySQL (via SQLAlchemy + PyMySQL)  
- **Visualization**: Seaborn, Matplotlib  
- **Pipeline**: Scikit-learn `Pipeline` & `ColumnTransformer`  

## 📂 Project Structure
```
├── data
│   └── AirTraffic_Passenger_Statistics.csv
├── notebooks
│   └── Hierarchical_Clustering.ipynb
├── reports
│   ├── Assignement_3.html
│   └── Project_Charter.md
├── images
│   └── plots.png
├── README.md
├── requirements.txt
└── LICENSE
```

## 📊 Key Insights
- **United Airlines** dominates passenger traffic, followed by American, SkyWest, and Delta.  
- Passenger traffic is **seasonal** with peaks in July–August and December.  
- **Terminal allocation** is uneven → potential for optimization.  
- Passenger demand grew consistently till 2015 (2016 dip due to incomplete data).
- 
## 📜 Project Charter
For detailed documentation including:

- **Business Problem**
- **High-Level Solution**
- **Objectives & Constraints**
- **Success Criteria** (Business, ML, Economic)
- **Data Dictionary**

👉 Please check the [Project_Charter.md](./Project_Charter.md) file in this repository.

## 📸 Sample Visualizations
- Dendrogram (Hierarchical Clustering)
-  <img width="555" height="441" alt="image" src="https://github.com/user-attachments/assets/cd8ee07e-48b2-4176-ab87-ee95c54d007f" />

- Top Airlines by Passenger Count (Pie Chart)
- <img width="613" height="409" alt="image" src="https://github.com/user-attachments/assets/97084e1a-c7fe-495a-af98-d8fe47d99ada" />

- Seasonal Trends (Bar Plot)
- <img width="554" height="453" alt="image" src="https://github.com/user-attachments/assets/7d9d2bab-6cbf-4088-bc8a-2568c2dd2424" />
- <img width="1586" height="797" alt="image" src="https://github.com/user-attachments/assets/bf60a93f-db82-4c41-89ad-ca09e1b3b25f" />



*(Add screenshots in `/images` and embed here)*

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/hierarchical-clustering-airline.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the notebook:
   ```bash
   jupyter notebook notebooks/Hierarchical_Clustering.ipynb
   ```

## 📌 Future Improvements
- Add **silhouette plots** and **cluster heatmaps**.  
- Deploy clustering results into a **dashboard** (Power BI / Streamlit).  
- Automate pipeline with Airflow or MLflow for production use.  

## 📝 Author
**Anshuman Acharya**  
🔗 [LinkedIn](https://linkedin.com/in/anshuman-a-acharya) | [Portfolio](https://anshux01.github.io/Portfolio/)  
