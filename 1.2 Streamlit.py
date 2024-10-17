import streamlit as st
import pickle
import pandas as pd

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit app title
st.title("Default Prediction")

# Input fields (only three features)
age = st.number_input("Enter Age", min_value=0, max_value=120, value=25)
annuity = st.number_input("Enter Annuity", min_value=0, max_value=100000, value=10000)
num_loans = st.number_input(
    "Enter Number of Loans", min_value=0, max_value=100, value=10
)

# Default values for other features not included in the UI
total_debit = 50000  # Example default value
total_credit_amt = 250000  # Example default value
ext_source_1 = 0.5
ext_source_2 = 0.5
ext_source_3 = 0.5
ext_source_mean = (ext_source_1 + ext_source_2 + ext_source_3) / 3
annual_payment_to_credit_ratio = 0.3
years_id_publish = 10
goods_price = 100000
annuity_to_income_ratio = 0.4
organization_type = "Self-employed"
years_registration = 5
years_last_phone_change = 3
years_employed = 15
years_employed_age_product = age * years_employed
income_to_age_ratio = 0.6
region_population_relative = 0.1
total_num_months = 60
total_sum_statuses = 5
avg_max_dpd = 30
total_num_closed = 4
total_num_unknown = 1
num_active_loans = 3
debt_credit_ratio = 0.4
total_overdue = 1000
max_overdue = 50
avg_days_overdue = 10
num_prolonged_loans = 2
num_previous_applications_x = 3
avg_annuity_amount = 20000
avg_days_decision = 40
max_days_decision = 60
min_days_decision = 10
sum_cnt_payment = 25
range_days_first_due = 30
range_days_last_due = 120
num_previous_applications_y = 1
sum_amt_instalment = 20000
avg_amt_instalment = 5000
sum_amt_payment = 21000
avg_amt_payment = 5000
max_amt_payment = 6000
min_amt_payment = 4000
sum_amt_payment_sum_amt_instalment = sum_amt_payment / sum_amt_instalment
mean_amt_payment_mean_amt_instalment = avg_amt_payment - avg_amt_instalment

# Prediction logic
if st.button("Predict"):
    input_data = pd.DataFrame(
        {
            "Age": [age],
            "AMT_ANNUITY": [annuity],
            "NUM_LOANS": [num_loans],
            # Default values for other features
            "TOTAL_DEBIT": [total_debit],
            "TOTAL_CREDIT_AMT": [total_credit_amt],
            "EXT_SOURCE_1": [ext_source_1],
            "EXT_SOURCE_2": [ext_source_2],
            "EXT_SOURCE_3": [ext_source_3],
            "EXT_SOURCE_MEAN": [ext_source_mean],
            "ANNUAL_PAYMENT_TO_CREDIT_RATIO": [annual_payment_to_credit_ratio],
            "YEARS_ID_PUBLISH": [years_id_publish],
            "AMT_GOODS_PRICE": [goods_price],
            "ANNUITY_TO_INCOME_RATIO": [annuity_to_income_ratio],
            "ORGANIZATION_TYPE": [organization_type],
            "YEARS_REGISTRATION": [years_registration],
            "YEARS_LAST_PHONE_CHANGE": [years_last_phone_change],
            "YEARS_EMPLOYED_AGE_PRODUCT": [years_employed_age_product],
            "INCOME_TO_AGE_RATIO": [income_to_age_ratio],
            "REGION_POPULATION_RELATIVE": [region_population_relative],
            "TOTAL_NUM_MONTHS": [total_num_months],
            "TOTAL_SUM_STATUSES": [total_sum_statuses],
            "AVG_MAX_DPD": [avg_max_dpd],
            "TOTAL_NUM_CLOSED": [total_num_closed],
            "TOTAL_NUM_UNKNOWN": [total_num_unknown],
            "NUM_ACTIVE_LOANS": [num_active_loans],
            "DEBT_CREDIT_RATIO": [debt_credit_ratio],
            "TOTAL_OVERDUE": [total_overdue],
            "MAX_OVERDUE": [max_overdue],
            "AVG_DAYS_OVERDUE": [avg_days_overdue],
            "NUM_PROLONGED_LOANS": [num_prolonged_loans],
            "NUM_PREVIOUS_APPLICATIONS_x": [num_previous_applications_x],
            "AVG_ANNUITY_AMOUNT": [avg_annuity_amount],
            "AVG_DAYS_DECISION": [avg_days_decision],
            "MAX_DAYS_DECISION": [max_days_decision],
            "MIN_DAYS_DECISION": [min_days_decision],
            "SUM_CNT_PAYMENT": [sum_cnt_payment],
            "RANGE_DAYS_FIRST_DUE": [range_days_first_due],
            "RANGE_DAYS_LAST_DUE": [range_days_last_due],
            "NUM_PREVIOUS_APPLICATIONS_y": [num_previous_applications_y],
            "SUM_AMT_INSTALMENT": [sum_amt_instalment],
            "AVG_AMT_INSTALMENT": [avg_amt_instalment],
            "SUM_AMT_PAYMENT": [sum_amt_payment],
            "AVG_AMT_PAYMENT": [avg_amt_payment],
            "MAX_AMT_PAYMENT": [max_amt_payment],
            "MIN_AMT_PAYMENT": [min_amt_payment],
            "SUM_AMT_PAYMENT/SUM_AMT_INSTALMENT": [sum_amt_payment_sum_amt_instalment],
            "MEAN_AMT_PAYMENT-MEAN_AMT_INSTALMENT": [
                mean_amt_payment_mean_amt_instalment
            ],
        }
    )

    # Make prediction
    prediction = model.predict(input_data)

    # Show result
    default_result = "YES" if prediction[0] == 1 else "NO"
    st.write(f"Default: {default_result}")
