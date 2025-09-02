# Project Charter – Hierarchical Clustering on Airline Passenger Data

**Name:** Anshuman Acharya  
**Batch ID:** DS/DA 16/06/2025 10AM HYD  
**Topic:** Hierarchical Clustering  

---

## 1. Business Understanding
**Problem:** Airlines face challenges in terminal allocation and operations, causing inefficiencies and passenger dissatisfaction.  
**Objective:** Maximize operational efficiency and financial health using clustering-based segmentation.  
**Constraints:** Maintain passenger experience while increasing efficiency.  

**Success Criteria:**  
- **Business:** Improve operational efficiency by 10–12%  
- **ML:** Silhouette Score ≥ 0.7  
- **Economic:** Hypothetical revenue growth by ≥ 8%  

---

## 2. Data Understanding
**Source:** AirTraffic_Passenger_Statistics.csv  
**Shape:** 15,007 rows × 9 columns  
**Observations:**  
- Null values in airline IATA codes  
- Skewed passenger count distribution  
- Seasonal peaks (July, August, December)  
- Growth until 2015; dip in 2016 (data issue)  
 # Data Dictionary

| Field              | Description                         | Variable Type     | Scale   | Example Value   | Additional Information                          |
|--------------------|-------------------------------------|-------------------|---------|-----------------|-----------------------------------------------|
| Activity Period          | Unique Period identifier (YYYYMM)                     | continuous         | Interval| 200507            | Represented Year and Month combined (e.g:,200507 = July 2005)  |
| Operating Airline         | Name of the airline                  | Discrete      | Nominal | ATA Airlines          | Airline Company Operating the Flight           |
| Operating Airline IATA Code         | IATA code of the airline                | Discrete       | Nominal |  TZ          | Two-character Airline code                             |
| GEO Region       |  Geographic region of operation               | Discrete      | Nominal | US             | Region code (e.g., US, International, Asia, etc.)        |
| Terminal              | Airport Terminal           | Discrete       | Nominal   | Terminal 1       | Terminal used for boarding/departure        |
|Boarding Area        | Boarding Gate/Area in Terminal          | Discrete         | Nominal   | B             | Subdivison Of terimanal                      |
| Passenger Count  |     Number of Passengers          | Continuous      | Ratio | 27,271       | Non-negative integer, zero is meanigful                       |
| Year    | Year Of Operation | Continuous       | Interval| 2005             | Extracted From Activity Period      |
| Month         | Month Of Operation            | Discrete      | Ordinal | July          | Names of months, Natural order (Jan - Dec)               |

| 15007 x 9 |
|-----------|

------------------
---

## 3. Data Preparation
- Removed duplicates and null handling  
- Feature Engineering: Month → numeric + cyclical (sin/cos)  
- Winsorization for outliers  
- One-Hot Encoding for categorical data  
- StandardScaler for normalization  

---

## 4. Modeling
- Technique: Hierarchical Clustering (Agglomerative)  
- Metrics: Euclidean Distance, Ward/Complete Linkage  
- Optimal Clusters: 5 (based on dendrogram + silhouette score)  

---

## 5. Evaluation
- **Silhouette Score ≥ 0.7** achieved  
- Business Insights:  
  - United Airlines leads market share  
  - Strong seasonality in demand  
  - Unequal terminal distribution  

---

## 6. Deployment (Future Scope)
- Store clustered data in MySQL for BI dashboards  
- Develop **interactive dashboards** (Power BI / Streamlit)  
- Automate pipeline for monthly retraining  

---

## 7. Monitoring & Maintenance
- Monitor silhouette score monthly  
- Refresh clusters with new passenger data  
- Trigger retraining if silhouette score drops < 0.7  

---

## Deliverables
- Notebook: Hierarchical_Clustering.ipynb  
- Report: Assignement_3.html  
- Project Charter: Project_Charter.md  
- GitHub Repo: With README, requirements.txt, LICENSE  

---

## Author
**Anshuman Acharya**  
🔗 [LinkedIn](https://linkedin.com/in/anshuman-a-acharya) | [Portfolio](https://anshux01.github.io/Portfolio/)  
