import streamlit as st
from utils.supabase_client import get_supabase

supabase = get_supabase()

st.title("Issued Contracts")

contracts = supabase.table("contracts").select("*").execute().data

for contract in contracts:
    st.subheader(f"Contract: {contract['id']}")
    st.write("Status:", contract["status"])
    st.write("Compliance:", contract["compliance_status"])

    with st.expander("View contract"):
        st.write(contract["contract_body"])

    if contract["status"] == "draft":
        if st.button(f"Mark as approved - {contract['id']}"):
            supabase.table("contracts").update({
                "status": "approved",
                "compliance_status": "approved"
            }).eq("id", contract["id"]).execute()

            st.success("Contract approved.")
