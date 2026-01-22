# Product_Sales_Forecasting

## Project Overview
This project focuses on forecasting retail product sales using historical transactional data.  
The goal is to help retail businesses improve inventory planning, budgeting, staffing, 
and strategic decision-making through accurate sales forecasting.

## Objective & Evaluation Metric
The objective is to build reliable forecasting models for:

• Sales  
• Number of Orders  

Model performance is evaluated using **MAPE (Mean Absolute Percentage Error)**

**Final Model Performance**

• Order Forecasting: **MAPE = 0.1509 (~15%)**  
• Sales Forecasting: **MAPE = 0.1973 (~19%)**

## Dataset Summary
The dataset contains:

Store ID, Store Type, Location Type, Region Code, Date, Holiday flag, Discount flag,  
Number of Orders, and Sales Amount.

## EDA & Hypothesis Findings

• Discounts significantly increase both orders and sales  
• Holidays generally show lower sales compared to normal days  
• Store Type, Location, and Region have strong influence on performance  
• Clear seasonal patterns are observed across months and days  
• Data is suitable for time-series forecasting

## Machine Learning Approach

• Data cleaning and preprocessing  
• Feature engineering  
• Time-series modeling (SARIMAX)  
• Model selection using MLflow  
• Forecast evaluation using MAPE  

## Key Insights

• Discounts drive strong business uplift  
• Holidays reduce customer activity  
• Sales behaviour varies across stores and regions  
• Strong seasonal demand patterns exist

## Submission Links
1. Tableau Dashboard includes:

     • Sales and Order Trends  
     • Regional Analysis  
     • Discount Impact  
     • Forecast Visualization  
     Tableau Dashboard: https://public.tableau.com/shared/7CMSJT3RF?:display_count=n&:origin=viz_share_link

2. Technical Blog on Medium: https://medium.com/@sravanikunapaneni08/product-sales-forecasting-using-machine-learning-ae388a6d97d5
   


