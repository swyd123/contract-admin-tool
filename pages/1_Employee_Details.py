import streamlit as st

from utils.supabase_client import get_supabase
from utils.award_rates import get_award_rate

supabase = get_supabase()

from utils.award_rates import get_award_rate

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
        "Level 1",
        "Level 2.1",
        "Level 2.2",
        "Level 3.1",
        "Level 3.2",
        "Level 3.3",
        "Level 3.4",
        "Level 4A.1",
        "Level 4A.2",
        "Level 4B.1",
        "Level 4B.2",
        "Level 5.1",
        "Level 5.2",
        "Level 5.3",
        "Level 6.1",
        "Level 6.2",
        "Director Level 1",
        "Director Level 2",
        "Director Level 3"
    ]
)

employment_type = st.selectbox(
    "Employment type",
    ["full-time", "part-time", "casual"]
)

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
