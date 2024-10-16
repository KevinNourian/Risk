import streamlit as st
import pickle
import pandas as pd

with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Default Prediction")

age = st.number_input("Enter Age", min_value=0, max_value=120, value=25)
annuity = st.number_input("Enter Annuity", min_value=0, max_value=100000, value=10000)
num_loans = st.number_input(
    "Enter Number of Loans", min_value=0, max_value=100, value=10
)
total_debit = st.number_input(
    "Enter Total Debit", min_value=0, max_value=100000, value=10000
)
ext_source_3 = st.number_input(
    "Enter External Source 3", min_value=0.0, max_value=1.0, value=0.5
)

if st.button("Predict"):
    input_data = pd.DataFrame(
        {
            "ANNUITY_TO_CREDIT_RATIO": [annuity / total_debit],
            "EXT_SOURCE_1": [ext_source_1],
            "EXT_SOURCE_2": [ext_source_2],
            "EXT_SOURCE_3": [ext_source_3],
            "EXT_SOURCE_MEAN": [ext_source_mean],
            "ANNUAL_PAYMENT_TO_CREDIT_RATIO": [annual_payment_to_credit_ratio],
            "Age": [age],
            "YEARS_ID_PUBLISH": [years_id_publish],
            "AMT_ANNUITY": [annuity],
            "AMT_GOODS_PRICE": [goods_price],
            "ANNUITY_TO_INCOME_RATIO": [annuity_to_income_ratio],
            "ORGANIZATION_TYPE": [organization_type],
            "YEARS_REGISTRATION	": [years_registration],
            "YEARS_LAST_PHONE_CHANGE": [years_last_phone_change],
            "YEARS_EMPLOYED_AGE_PRODUCT": [years_employed_age_product],
            "INCOME_TO_AGE_RATIO": [income_to_age_ratio],
            "REGION_POPULATION_RELATIVE": [region_population_relative],
            "NUM_LOANS": [num_loans],
            "TOTAL_NUM_MONTHS": [total_num_months],
            "TOTAL_SUM_STATUSES": [total_sum_statuses],
            "AVG_MAX_DPD": [avg_max_dpd],
            "TOTAL_NUM_CLOSED": [total_num_closed],
            "TOTAL_NUM_UNKNOWN": [total_num_unknown],
            "NUM_ACTIVE_LOANS": [num_active_loans],
            "TOTAL_DEBIT": [total_debit],
            "TOTAL_CREDIT_AMT": [total_credit_amt],
            "DEBT_CREDIT_RATIO": [debt_credit_ratio],
            "TOTAL_OVERDUE": [total_overdue],
            "TOTAL_DEBIT": [total_debit],
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

    prediction = model.predict(input_data)

    default_result = "YES" if prediction[0] == 1 else "NO"
    st.write(f"Default: {default_result}")
