import streamlit as st
from utils.supabase_client import get_supabase
from utils.compliance import check_rate, check_employment_type, check_information_statements

supabase = get_supabase()

st.title("Compliance Check")

employees = supabase.table("employees").select("*").execute().data

employee_names = {
    f"{e['first_name']} {e['last_name']}": e for e in employees
}

selected = st.selectbox("Select employee", list(employee_names.keys()))

if selected:
    employee = employee_names[selected]

    rates = supabase.table("award_rates") \
        .select("*") \
        .eq("award", employee["award"]) \
        .eq("employment_type", employee["employment_type"]) \
        .execute().data

    if not rates:
        st.error("No award rate found. Manual review required.")
    else:
        minimum_rate = rates[0]["minimum_hourly_rate"]

        rate_check = check_rate(employee["hourly_rate"], minimum_rate)
        type_check = check_employment_type(
            employee["employment_type"],
            employee["ordinary_hours"]
        )

        st.write("### Results")
        st.write(rate_check)
        st.write(type_check)

        st.write("### Required information statements")
        st.write(check_information_statements(employee["employment_type"]))
