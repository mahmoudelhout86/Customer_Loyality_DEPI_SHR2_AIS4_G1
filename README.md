# Customer Loyalty Analysis Project

This project focuses on analyzing customer loyalty using data from the **Elo Merchant Category Recommendation** competition hosted on Kaggle. The goal is to predict customer loyalty scores based on transactional and merchant data, enabling personalized recommendations and improved customer engagement.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Table of Contents

1. Project Overview
2. Installation
3. Data Sources
4. Dataset Overview
5. Technologies Used
6. Team Members


------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Project Overview

    1.1 Objective

The primary objective of this project is to predict customer loyalty scores, which will help Elo (a Brazilian payment brand) recommend merchant categories to its users and enhance customer satisfaction.

    1.2 Scope

- Data preprocessing and feature engineering.

- Analyze transactional data to understand customer behavior.

- Visualization of key trends and insights.

- Build a predictive model to estimate customer loyalty scores.

- Provide actionable insights for personalized recommendations.

---------------------------------------------------------------------------------------------------------------------------------------------------

2. Installation

To run this project locally, follow these steps:

   a. Clone the Repository to your local storage

   b. Set Up a Python Environment.

   c. Install Dependencies pandas like numpy, pandas, scikit-learn, matplotlib, seaborn and others.

   d. Handle Large Files: The dataset includes large CSV files (e.g., historical_transactions.csv ~2.8 GB), you can download all data from link in the data source.


---------------------------------------------------------------------------------------------------------------------------------------------------------   

3. Data Sources

The dataset is sourced from the Elo Merchant Category Recommendation competition on Kaggle.  https://www.kaggle.com/c/elo-merchant-category-recommendation/data

---------------------------------------------------------------------------------------------------------------------------------------------------------   

4. Dataset Overview

The data provided contains the transaction data of up to 3 months for each card ID. It also contains the merchant data based on the merchants involved in these transactions.The dataset consists of several files:

   a. Data_Dictionary.xlsx:
This file contains the datafield description for each csv file.

   b. train.csv and test.csv:
These files contain the Card IDs(card_id) and the information about the cards.
They also contain the target variable(loyalty score) that needs to be predicted. 
Below are the descriptions for each of the columns:
card_id → Unique card identifier
first_active_month → month of first purchase in 'YYYY-MM' format
feature_1 → Anonymized card categorical feature
feature_2→ Anonymized card categorical feature
feature_3 → Anonymized card categorical feature
target → Loyalty numerical score calculated 2 months after historical and evaluation period


   c. historical_transactions.csv and new_merchant_transactions.csv: 
These files contain the transactions data. 
They contain information about transactions for each card. 
Below are the descriptions for each of the columns:
card_id → Card identifier
month_lag → month lag to reference date
purchase_date → Purchase date
authorized_flag → 'Y' if approved, 'N' if denied
category_3 → anonymized category
installments → number of installments of purchase
category_1 → anonymized category
merchant_category_id → Merchant category identifier(anonymized)
subsector_id → Merchant category group identifier(anonymized)
merchant_id → Merchant identifier(anonymized)
purchase_amount → Normalized purchase amount
city_id → City identifier(anonymized)
state_id → State identifier (anonymized)
category_2 → anonymized category

   d. merchants.csv:  
This file contains the additional information of the merchants involved in the transactions. 
Below are the descriptions for each of the columns:
merchant_id → Unique merchant identifier
merchant_group_id → Merchant group(anonymized)
merchant_category_id → Unique identifier for merchant category (anonymized)
subsector_id → Merchant category group (anonymized)
numerical_1 → anonymized measure
numerical_2 → anonymized measure
category_1 → anonymized category
category_2 → anonymized category
category_4 → anonymized category
city_id → City identifier(anonymized)
most_recent_sales_range → Range of revenue (monetary units) in last active month (A > B > C > D > E)
most_recent_sales_range → Range of revenue (monetary units) in last active month (A > B > C > D > E)
most_recent_purchases_range → Range of quantity of transactions in last active month (A > B > C > D > E)
avg_sales_lag3 → Monthly average of revenue in last 3 months divided by revenue in last active month
avg_purchases_lag3 → Monthly average of transactions in last 3 months divided by transactions in last active month
active_months_lag3 → Quantity of active months within last 3 months
avg_sales_lag6 → Monthly average of revenue in last 6 months divided by revenue in last active month
avg_purchases_lag6 → Monthly average of transactions in last 6 months divided by transactions in last active month
active_months_lag6 → Quantity of active months within last 6 months
avg_sales_lag12 → Monthly average of revenue in last 12 months divided by revenue in last active month
avg_purchases_lag12 → Monthly average of transactions in last 12 months divided by transactions in last active month
active_months_lag12 → Quantity of active months within last 12 month

---------------------------------------------------------------------------------------------------------------------------------------------------------   

5. Technologies Used:

   a. Python (Numpy, Pandas, Scikit-learn, TensorFlow, SpaCy)

   b. Machine Learning (ML) models, the basic regression algorithms for training the model which are as follows:
                · Linear Regression
                · Ridge
                · Lasso
                · Gradient Boosting
                · Decision Tree Regressor
                · Random Forest Regressor
                · Ada Boost Regressor
                · Light GBM
                · XG Boost
                · KNN

   c. GitHub Projects (for task management).

---------------------------------------------------------------------------------------------------------------------------------------------------------   

6. Team Members:

   a. Mahmoud Emam Elhout

   b. Tarek Ahmed Ali

   c. Hazem Mohamed Samy

   d. Asmaa Gamal AbdElnasser
