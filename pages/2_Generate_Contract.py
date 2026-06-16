import streamlit as st
from utils.supabase_client import get_supabase
from utils.contract_generator import generate_contract

supabase = get_supabase()

st.title("Generate Contract")

employees = supabase.table("employees").select("*").execute().data

employee_names = {
    f"{e['first_name']} {e['last_name']}": e for e in employees
}

selected = st.selectbox("Select employee", list(employee_names.keys()))

if selected:
    employee = employee_names[selected]

    template_map = {
        "full-time": "full_time_contract.md",
        "part-time": "part_time_contract.md",
        "casual": "casual_contract.md",
        "fixed-term": "part_time_contract.md"
    }

    template = template_map[employee["employment_type"]]

    contract_body = generate_contract(template, employee)

    st.text_area("Contract preview", contract_body, height=500)

    if st.button("Save draft contract"):
        supabase.table("contracts").insert({
            "employee_id": employee["id"],
            "contract_type": employee["employment_type"],
            "status": "draft",
            "contract_body": contract_body,
            "compliance_status": "pending review"
        }).execute()

        st.success("Draft contract saved.")
