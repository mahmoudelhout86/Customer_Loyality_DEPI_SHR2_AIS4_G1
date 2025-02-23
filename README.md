# Customer Loyalty Analysis Project

This project focuses on analyzing customer loyalty using data from the **Elo Merchant Category Recommendation** competition hosted on Kaggle. The goal is to predict customer loyalty scores based on transactional and merchant data, enabling personalized recommendations and improved customer engagement.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Table of Contents

1. Project Overview
2. Installation
3. Data Sources
4. Dataset Overview


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


---------------------------------------------------------------------------------------------------------------------------------------------------------   

3. Data Sources

The dataset is sourced from the Elo Merchant Category Recommendation competition on Kaggle.

---------------------------------------------------------------------------------------------------------------------------------------------------------   

4. Dataset Overview

The dataset consists of several files:

train.csv: Contains the training data with the target variable (target).

card_id: Unique identifier for each customer card.

target: The target variable (loyalty score) to predict.

test.csv: Contains the test data (without the target variable).

card_id: Unique identifier for each customer card.

historical_transactions.csv: Contains historical transaction data for each card.

card_id: Unique identifier for the customer card.

purchase_date: Date and time of the transaction.

purchase_amount: Amount spent in the transaction.

merchant_category_id: Category of the merchant.

merchant_id: Unique identifier for the merchant.

Other features like city_id, state_id, subsector_id, etc.

new_merchant_transactions.csv: Contains transactions from new merchants (similar structure to historical_transactions.csv).

merchants.csv: Contains additional information about merchants.

merchant_id: Unique identifier for the merchant.

merchant_category_id, merchant_group_id, subsector_id, etc.
