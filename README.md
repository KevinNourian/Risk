![Alt_Text](https://github.com/KevinNourian/Risk/blob/main/Images/risk.png)
# Project Files
**1.0 Overview:** This notebook familiarizes the reader with the goals, standards, biases and the basic characteristics of the data. </BR>
**2.0 Pre-Processing:** In this notebook, I cleaned the data to get it ready for the later parts of the project by removing inaccurate entries, infinity values, and features with just one value. I converted features with number of days to number of years</BR>
**3.0 EDA:** In this part of the project, I visually display interesting insights from the data in the main application_train table.</BR>
**4.0 Feature Engineering:** In this notebook, I utilized the existing features to create new features that proved to have much higher predictive value than the original features. </BR>
**5.0 Machine Learning Iterations:** In this part of the project, I utilized LightGBM's feature importance tool to identify the features with the most predictive power. With this tool, I identified 18 features with acceptable predictive values.</BR>
**6.0 Bureau:** In this notebook, I aggregated features in the bureau and bureau-balance tables and merged them into a table I called simply bureau. Through the aggregation new features were created that I later merged with the main application_train table. </BR>
**7.0 Previous:** In this part of the project, I aggregated features in the previous_payments table that I will merge with the main application_train table. The new aggregated features will prove to have good predictive capabilities.</BR>
**8.0 Installments:** In this notebook, I aggregated features in the installments_payments table that I will merge with the main application_train table. The new aggregated features will prove to have good predictive capabilities.</BR>
**9.0 Hypothesis Tests:** In this part of the project, I conducted two important hypothesis tests, one related to income type and the other related to credit amount.</BR>
**10.0 Final Table:** In this part of the project, I merged 4 tables created in other parts of this project into one table to be ready for final modeling in Notebook 11.0.</BR>
**11.0 Final Modeling:** In this part of the project, I compared three models: Logistic Regression, Random Forest and LightGBM and compared their performance using ROC-AUC socres. LightGBM performed better than the other two models. I used Optuna for hyperparameter tuning of the LightGBM model and increaed performance slightly.</BR>
**12.0 Conclusions:** This notebook summarizes the conclusions that may be drawn from this report. It also outlines weaknesses and avenues for improvement.</BR>
**13.0 Deployment:** This notebook contains the link for the web application used for deployment.</BR>
**streamlit.py:** This code was used to deploy the model using the Streamlit application.</BR>

# Introduction
Risk management involves the identification, assessment, measurement, and management of potential risks. In the financial sector, investors take on risks with the expectation of receiving higher economic returns as compensation. This project will explore loan repayment rates as a key aspect of credit risk management. Specifically, we will examine the possibility of nonpayment, whether it pertains to future obligations or ongoing transactions.

# Datasets
**1. application_{train|test}:** This is the main table, broken into two files for Train (with TARGET) and Test(without TARGET).Static data for all applications. One row represents one loan in our datasample. </BR>
**2. bureau:** All client's previous credits provided by other financial institutions that were reported to Credit Bureau (for clients who have a loan in our sample). For every loan in our sample, there are as many rows as number of credits theclient had in Credit Bureau before the application date. </BR>
**3. bureau_balance:** Monthly balances of previous credits in Credit Bureau. The table has one row for each month of history for every previous creditreported to Credit Bureau – i.e the table has (#loans in sample * # of relativeprevious credits * # of months where we have some history observable for theprevious credits) rows. </BR>
**4. POS_CASH_balance:** Monthly balance snapshots of previous POS (point of sale) and cash loans that the applicant had with Home Credit. This table has one row for each month of history of every previous credit in Home Credit (consumer credit and cash loans) related to loans in our sample –i.e. the table has (#loans in sample * # of relative previous credits * # ofmonths in which we have some history observable for the previous credits) rows.</BR>
**5. credit_card_balance:** Monthly balance snapshots of previous credit cards that the applicant has with Home Credit. The table has one row for each month in the history of every previous credit inHome Credit (consumer credit and cash loans) related to loans in our sample –i.e. the table has (#loans in sample * # of relative previous credit cards * #of months where we have some history observable for the previous credit card)rows.</BR>
**6. previous_application:** All previous applications for Home Credit loans of clients who have loans in our sample. There is one row for each previous application related to loans in our datasample.</BR>
**7. installments_payments:** Repayment history for the previously disbursed credits in Home Credit related to the loans in our sample. There is a) one row for every payment that was made plus b) one row each formissed payment. One row is equivalent to one payment of one installment OR one installmentcorresponding to one payment of one previous Home Credit credit related to loansin our sample.</BR>
**8. HomeCredit_columns_description:** This file contains descriptions for the columns in the various data files.


# Goals
**Interpretability:**  Since this project is aimed at an industry where transparency is crucial, my goal is to make predictions with as few features as possible so they can be explained to both stakeholders and clients in an easy and clear manner.  </BR>
**Error Rate:** The cost of making an error can be very high. This is due to the large amounts of funds associated with each loan. We do not want the model to miss out on potential defaulters which could incur huge financial losses. My second goal is to predict defaults with a ROC AUC score of 75% or higher.


# Technical Requirements
1. Exploratory data analysis
2. Pre-Processing of the data
3. Application of various machine learning models to predict which clients will default on their loan.
4. Clear explanations of findings
5. Final conclusions
6. Suggestions on how the analysis can be improved


# Standards
> **Standard 1:** My standard for an acceptable ROC AUC is 75%. <BR>
> **Standard 2:** My standard for colinearity is a Pearson correlation coefficient of approximately 80%. <BR> 


# Biases
There could be many hidden biases in the way the data is collected, which is not clear from the information provided. In addition, the large amount of missing data provides another level of bias.


# Domain Knowledge
I have no experience with financial data. I may have overlooked parts of the data that may have been most important and I may have given importance to parts that may have had little significance. 


# Conclusions
>* **The Analysis of the Data:** I reviewed approximately 50,000,000 datapoints in 5 tables related to clients in the Home Credit Default Risk Assessment dataset. <br> 
>* **The Goal of the Project:** The goal of this project was to find a model that could predict if a client will default on a loan. I further wanted to make this determination with as few feature and in the most transparent manner possible.<br>
>* **Missing Data:** There was a great deal of missing data in many of the features. I imputed this missing data by assigning a random number to the numerical columns and labeling missing categorical data with the text, "UNKNOWN"."  <br>
>* **Models:** I utilized the following models: Logistic Regression, Random Forest, Light Gradient Boosting Machine (LGBM).
>* **Logistic Regression:** ROC-AUC Score: 0.63.  <br>
>* **Random Forest:** ROC-AUC Score: 0.73.   <br>
>* **XGBClassifier:** ROC-AUC Score: 0.72.   <br>
>* **Light Gradient Boosting (LGBM):** OC-AUC Score: 0.74.   <br>
>* **OPTUNA:** I used OPTUNA to tune the hyperparameters of the LGBM model. <br>
>* **Final Model (LGBM) with Hyperparameter Tuning:** ROC-AUC Score: 0.77.<br>


# Suggestions for Improvement
>* **Domain Knowledge:** It is best if the data scientist has adequate domain knowledge on the topic of the analysis. I do not have any expertise in the financial sector. By doing some research, I tried to augment this lack. However, there may be parts of the data that I have overlooked that may have been important and I may have given importance to parts that may have had little significance. <br>
>* **More Complete Data:** As mentioned earlier, there was missing data in many of the features. Less missing data could have improved the performance of the models.<br>  
>* **Pandas:** Continue to learn to utilize more optimized Pandas techniques and algorithms.<br>
>* **Seaborn and Matplotlib:** Continue to improve my knowledge of Seaborn and Matplotlib for creating visualizations. <br>
>* **Machine Learning:** Continue to improve on my capabilities with various models. <br>
>* **Python Code:** Continue to write better and more efficient Python code. <br>
>* **Clean Code:** Continue to adhere to the principles of writing clean code. <br>
>* **Readability and Efficiency:** Continue to improve my skills to find the delicate balance between readability and efficiency in coding.<br>


# Requirements
altair==5.4.1 </BR>
attrs==24.2.0 </BR>
blinker==1.8.2 </BR>
cachetools==5.5.0</BR>
certifi==2024.8.30</BR>
charset-normalizer==3.4.0</BR>
click==8.1.7</BR>
colorama==0.4.6</BR>
feature-engine==1.8.1</BR>
gitdb==4.0.11</BR>
GitPython==3.1.43</BR>
idna==3.10</BR>
Jinja2==3.1.4</BR>
joblib==1.4.2</BR>
jsonschema==4.23.0</BR>
jsonschema-specifications==2024.10.1</BR>
lightgbm==4.5.0</BR>
markdown-it-py==3.0.0</BR>
MarkupSafe==3.0.1</BR>
mdurl==0.1.2</BR>
narwhals==1.9.4</BR>
numpy==2.1.2</BR>
packaging==24.1</BR>
pandas==2.2.3</BR>
patsy==0.5.6</BR>
pillow==10.4.0</BR>
protobuf==5.28.2</BR>
pyarrow==17.0.0</BR>
pydeck==0.9.1</BR>
Pygments==2.18.0</BR>
python-dateutil==2.9.0.post0</BR>
pytz==2024.2</BR>
referencing==0.35.1</BR>
requests==2.32.3</BR>
rich==13.9.2</BR>
rpds-py==0.20.0</BR>
scikit-learn==1.5.2</BR>
scipy==1.14.1</BR>
six==1.16.0v
smmap==5.0.1</BR>
statsmodels==0.14.4</BR>
streamlit==1.39.0</BR>
tenacity==9.0.0</BR>
threadpoolctl==3.5.0</BR>
toml==0.10.2</BR>
tornado==6.4.1</BR>
typing_extensions==4.12.2</BR>
tzdata==2024.2</BR>
urllib3==2.2.3</BR>
watchdog==5.0.3</BR>