import streamlit as st
from utils.supabase_client import get_supabase

supabase = get_supabase()

st.title("Employee Details")

with st.form("employee_form"):
    first_name = st.text_input("First name")
    last_name = st.text_input("Last name")
    email = st.text_input("Email")
    role_title = st.text_input("Role title")

    employment_type = st.selectbox(
        "Employment type",
        ["full-time", "part-time", "casual", "fixed-term"]
    )

    award = st.selectbox(
        "Award",
        [
            "Children’s Services Award MA000120",
            "Educational Services Teachers Award",
            "Clerks Private Sector Award",
            "Manual review required"
        ]
    )

    classification = st.text_input("Classification")
    hourly_rate = st.number_input("Hourly rate", min_value=0.0, step=0.01)
    ordinary_hours = st.number_input("Ordinary hours per week", min_value=0.0, step=0.5)
    start_date = st.date_input("Start date")

    submitted = st.form_submit_button("Save employee")

if submitted:
    supabase.table("employees").insert({
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "role_title": role_title,
        "employment_type": employment_type,
        "award": award,
        "classification": classification,
        "hourly_rate": hourly_rate,
        "ordinary_hours": ordinary_hours,
        "start_date": str(start_date)
    }).execute()

    st.success("Employee saved.")
