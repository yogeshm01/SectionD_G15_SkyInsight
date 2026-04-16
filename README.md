# SectionD_G15_SkyInsight

## Project Overview

| Field | Details |
|---|---|
| **Project Title** | SkyInsight — Airline Passenger Satisfaction Analytics |
| **Sector** | Aviation / Airline Industry |
| **Team ID** | DVA-D-G15 |
| **Section** | Section D |
| **Faculty Mentor** | Archit Raj |
| **Institute** | Newton School of Technology |


---

### Team Members

| Role | Name | GitHub Username |
|---|---|---|
| Project Lead | Yogesh Mishra | `yogeshm01` |
| Data Lead | Yogesh Mishra | `yogeshm01` |
| ETL Lead | Yogesh Mishra | `yogeshm01` |
| Analysis Lead | Mohammad Affan anas | `affan80` |
| Visualization Lead | Mohammad Affan anas | `affan80` |
| Strategy Lead | Aditi Singh | `aditisingh60` |
| PPT & Quality Lead | Bhavya punj | `username` |


---

## Business Problem

Airlines operate in a highly competitive industry where customer satisfaction directly impacts brand loyalty and future bookings. However, airlines lack clarity on which service attributes (such as seat comfort, food quality, and in-flight service) most strongly influence passenger perception and recommendation behavior.

---

### Core Business Question

> Which service attributes have the greatest impact on passenger ratings and recommendation behavior across different customer segments?

---

### Decision Supported

> This analysis will enable airline stakeholders to prioritize improvements in key service areas, optimize resource allocation, and enhance customer experience strategies to improve overall ratings and recommendation rates.

---

## Dataset

| Attribute | Details |
|---|---|
| **Source Name** | Kaggle — Airline Reviews Dataset |
| **Direct Access Link** | https://www.kaggle.com/datasets/juhibhojani/airline-reviews |
| **Row Count** | 23,000+ |
| **Column Count** | 20+ |
| **Format** | CSV |

---

### Key Columns Used

| Column Name | Description | Role |
|---|---|---|
| Airline Name | Airline identifier | Comparison |
| Overall Rating | Rating out of 10 | KPI |
| Seat Comfort | Comfort rating | Service analysis |
| Food & Beverages | Food rating | KPI |
| Inflight Service | Service rating | KPI |
| Value for Money | Value perception | KPI |
| Type of Traveller | Passenger type | Segmentation |
| Seat Type | Class type | Segmentation |
| Recommended | Yes/No | KPI |
| Review | Text data | Sentiment analysis |

---

## KPI Framework

| KPI | Definition |
|---|---|
| Passenger Recommendation Rate (%) | % of passengers recommending airline |
| Average Overall Rating | Mean rating |
| Average Service Score | Avg of service ratings |
| Sentiment Score | Derived from text |
| Segment Satisfaction Score | Group-wise analysis |

---

## Tableau Dashboard

| Item | Details |
|---|---|
| Dashboard URL | _Add link_ |
| Executive View | KPI summary |
| Operational View | Service vs rating analysis |
| Filters | Airline, Seat Type, Traveller Type |

---

## Key Insights

1. Service quality impacts recommendation  
2. Seat comfort strongly affects ratings  
3. Economy passengers show lower satisfaction  
4. Food quality impacts perception  
5. Airline performance varies  

---

## Recommendations

| # | Recommendation |
|---|---|
| 1 | Improve in-flight service quality |
| 2 | Upgrade seat comfort |
| 3 | Enhance economy experience |
| 4 | Improve food quality |
| 5 | Benchmark top airlines |

---

## Expected Repository Structure

```text
SectionD_G15_SkyInsight/
├── README.md
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_extraction.ipynb
│   ├── 02_cleaning.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_statistical_analysis.ipynb
│   └── 05_final_load_prep.ipynb
├── scripts/
│   └── etl_pipeline.py
├── tableau/
│   ├── screenshots/
│   └── dashboard_links.md
├── reports/
│   ├── project_report.pdf
│   └── presentation.pdf
├── docs/
│   └── data_dictionary.md