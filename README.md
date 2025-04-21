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

## 1. Project Overview

    ### 1.1 Objective

The primary objective of this project is to predict customer loyalty scores, which will help Elo (a Brazilian payment brand) recommend merchant categories to its users and enhance customer satisfaction.

    ### 1.2 Scope

- Data preprocessing and feature engineering.

- Analyze transactional data to understand customer behavior.

- Visualization of key trends and insights.

- Build a predictive model to estimate customer loyalty scores.

- Provide actionable insights for personalized recommendations.

---------------------------------------------------------------------------------------------------------------------------------------------------

## 2. Installation

To run this project locally, follow these steps:

   ### a. Clone the Repository to your local storage

   ### b. Set Up a Python Environment.

   ### c. Install Dependencies pandas like numpy, pandas, scikit-learn, matplotlib, seaborn and others.

   ### d. Handle Large Files: The dataset includes large CSV files (e.g., historical_transactions.csv ~2.8 GB), you can download all data from link in the data source.


---------------------------------------------------------------------------------------------------------------------------------------------------------   

## 3. Data Sources

The dataset is sourced from the Elo Merchant Category Recommendation competition on Kaggle.  https://www.kaggle.com/c/elo-merchant-category-recommendation/data

---------------------------------------------------------------------------------------------------------------------------------------------------------   

## 4. Dataset Overview

The data provided contains the transaction data of up to 3 months for each card ID. It also contains the merchant data based on the merchants involved in these transactions.The dataset consists of several files:

   ### a. Data_Dictionary.xlsx:

This file contains the datafield description for each csv file and descriptions for each of the columns.

   ### b. train.csv and test.csv:

These files contain the Card IDs(card_id) and the information about the cards.

They also contain the target variable(loyalty score) that needs to be predicted. 

   ### c. historical_transactions.csv and new_merchant_transactions.csv:
 
These files contain the transactions data. 

They contain information about transactions for each card. 


   ### d. new_merchant_transactions.csv:

The same data in historical_transactions.csv

   ### e. merchants.csv:  

This file contains the additional information of the merchants involved in the transactions.


---------------------------------------------------------------------------------------------------------------------------------------------------------   

## 5. Technologies Used:

   ### a. Python (Numpy, Pandas, Scikit-learn, TensorFlow, SpaCy)

   ### b. Machine Learning (ML) models, the basic regression algorithms for training the model which are as follows:
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

   ### c. GitHub Projects (for task management).

---------------------------------------------------------------------------------------------------------------------------------------------------------   

## 6. Team Members:

   ### a. Mahmoud Emam Elhout

   ### b. Tarek Ahmed Ali

   ### c. Hazem Mohamed Samy

   ### d. Asmaa Gamal AbdElnasser
