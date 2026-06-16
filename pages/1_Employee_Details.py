import streamlit as st

from utils.supabase_client import get_supabase
from utils.award_rates import get_award_rate

supabase = get_supabase()

st.title("Employee Details")

with st.form("employee_form"):
    first_name = st.text_input("First name")
    last_name = st.text_input("Last name")
    email = st.text_input("Email")
    role_title = st.text_input("Role title")

    award = st.selectbox(
        "Award",
        [
            "Children’s Services Award MA000120",
            "Educational Services Teachers Award",
            "Clerks Private Sector Award",
            "Manual review required"
        ]
    )

    classification = st.selectbox(
        "Classification",
        [
            "Level 1 - Introductory Educator",
            "Level 2 - Educator",
            "Level 3 - Qualified Educator",
            "Level 4 - Experienced Educator",
            "Level 5 - Advanced Educator",
            "Level 6 - Room Leader",
            "Level 7 - Assistant Director",
            "Level 8 - Director"
        ]
    )

    employment_type = st.selectbox(
        "Employment type",
        ["full-time", "part-time", "casual"]
    )

    ordinary_hours = st.number_input(
        "Ordinary hours per week",
        min_value=0.0,
        step=0.5
    )

    start_date = st.date_input("Start date")

    rate_record = get_award_rate(
        supabase,
        award,
        classification,
        employment_type
    )

    if rate_record:
        hourly_rate = rate_record["minimum_hourly_rate"]
        st.success(f"Generated hourly rate: ${hourly_rate:.2f}")
    else:
        hourly_rate = None
        st.error("No rate found for this award/classification/employment type. Manual review required.")

    submitted = st.form_submit_button("Save employee")

if submitted:
    if hourly_rate is None:
        st.error("Cannot save employee because no award rate was found.")
    else:
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

        st.success("Employee saved with generated award rate.")
