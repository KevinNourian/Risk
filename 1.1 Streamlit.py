import streamlit as st
import pickle
import pandas as pd

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Streamlit app title
st.title("Default Prediction")

# Input fields
age = st.number_input("Enter Age", min_value=0, max_value=120, value=25)
annuity = st.number_input("Enter Annuity", min_value=0, max_value=100000, value=10000)
num_loans = st.number_input(
    "Enter Number of Loans", min_value=0, max_value=100, value=10
)
total_debit = st.number_input(
    "Enter Total Debit", min_value=0, max_value=100000, value=10000
)
total_credit_amt = st.number_input(
    "Enter Total Credit Amount", min_value=0, max_value=1000000, value=50000
)
ext_source_1 = st.number_input(
    "Enter External Source 1", min_value=0.0, max_value=1.0, value=0.5
)
ext_source_2 = st.number_input(
    "Enter External Source 2", min_value=0.0, max_value=1.0, value=0.5
)
ext_source_3 = st.number_input(
    "Enter External Source 3", min_value=0.0, max_value=1.0, value=0.5
)
ext_source_mean = (ext_source_1 + ext_source_2 + ext_source_3) / 3

# Other user input fields for the model
annual_payment_to_credit_ratio = st.number_input(
    "Enter Annual Payment to Credit Ratio", min_value=0.0, max_value=10.0, value=0.5
)
years_id_publish = st.number_input(
    "Enter Years ID Published", min_value=0, max_value=50, value=5
)
goods_price = st.number_input(
    "Enter Goods Price", min_value=0, max_value=1000000, value=100000
)
annuity_to_income_ratio = st.number_input(
    "Enter Annuity to Income Ratio", min_value=0.0, max_value=10.0, value=0.5
)
organization_type = st.text_input("Enter Organization Type", value="Self-employed")
years_registration = st.number_input(
    "Enter Years Registration", min_value=0, max_value=50, value=5
)
years_last_phone_change = st.number_input(
    "Enter Years Since Last Phone Change", min_value=0, max_value=50, value=2
)
years_employed = st.number_input(
    "Enter Years Employed", min_value=0, max_value=50, value=10
)
years_employed_age_product = age * years_employed  # Calculated variable
income_to_age_ratio = st.number_input(
    "Enter Income to Age Ratio", min_value=0.0, max_value=10.0, value=0.5
)
region_population_relative = st.number_input(
    "Enter Region Population Relative", min_value=0.0, max_value=1.0, value=0.2
)

# More input fields for the rest of the variables
total_num_months = st.number_input(
    "Enter Total Number of Months", min_value=0, max_value=1000, value=60
)
total_sum_statuses = st.number_input(
    "Enter Total Sum Statuses", min_value=0, max_value=100, value=5
)
avg_max_dpd = st.number_input(
    "Enter Average Maximum DPD", min_value=0, max_value=1000, value=30
)
total_num_closed = st.number_input(
    "Enter Total Number of Closed Loans", min_value=0, max_value=100, value=3
)
total_num_unknown = st.number_input(
    "Enter Total Number of Unknown Loans", min_value=0, max_value=100, value=0
)
num_active_loans = st.number_input(
    "Enter Number of Active Loans", min_value=0, max_value=100, value=2
)
debt_credit_ratio = st.number_input(
    "Enter Debt to Credit Ratio", min_value=0.0, max_value=1.0, value=0.5
)
total_overdue = st.number_input(
    "Enter Total Overdue Amount", min_value=0, max_value=1000000, value=0
)
max_overdue = st.number_input(
    "Enter Maximum Overdue Amount", min_value=0, max_value=100000, value=30
)
avg_days_overdue = st.number_input(
    "Enter Average Days Overdue", min_value=0, max_value=1000, value=15
)
num_prolonged_loans = st.number_input(
    "Enter Number of Prolonged Loans", min_value=0, max_value=100, value=1
)

# Input fields for previous applications and payment details
num_previous_applications_x = st.number_input(
    "Enter Number of Previous Applications (X)", min_value=0, max_value=100, value=2
)
avg_annuity_amount = st.number_input(
    "Enter Average Annuity Amount", min_value=0, max_value=100000, value=10000
)
avg_days_decision = st.number_input(
    "Enter Average Days Decision", min_value=0, max_value=1000, value=20
)
max_days_decision = st.number_input(
    "Enter Maximum Days Decision", min_value=0, max_value=1000, value=50
)
min_days_decision = st.number_input(
    "Enter Minimum Days Decision", min_value=0, max_value=1000, value=5
)
sum_cnt_payment = st.number_input(
    "Enter Sum of Count Payment", min_value=0, max_value=1000, value=24
)
range_days_first_due = st.number_input(
    "Enter Range of Days for First Due", min_value=0, max_value=1000, value=30
)
range_days_last_due = st.number_input(
    "Enter Range of Days for Last Due", min_value=0, max_value=1000, value=180
)
num_previous_applications_y = st.number_input(
    "Enter Number of Previous Applications (Y)", min_value=0, max_value=100, value=1
)

# Instalment and payment details
sum_amt_instalment = st.number_input(
    "Enter Sum of Amount Instalment", min_value=0, max_value=1000000, value=20000
)
avg_amt_instalment = st.number_input(
    "Enter Average Amount Instalment", min_value=0, max_value=100000, value=5000
)
sum_amt_payment = st.number_input(
    "Enter Sum of Amount Payment", min_value=0, max_value=1000000, value=21000
)
avg_amt_payment = st.number_input(
    "Enter Average Amount Payment", min_value=0, max_value=100000, value=5000
)
max_amt_payment = st.number_input(
    "Enter Maximum Amount Payment", min_value=0, max_value=100000, value=6000
)
min_amt_payment = st.number_input(
    "Enter Minimum Amount Payment", min_value=0, max_value=100000, value=4000
)
sum_amt_payment_sum_amt_instalment = (
    sum_amt_payment / sum_amt_instalment
)  # Calculated variable
mean_amt_payment_mean_amt_instalment = (
    avg_amt_payment - avg_amt_instalment
)  # Calculated variable

# Prediction logic
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
            "YEARS_REGISTRATION": [years_registration],
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
