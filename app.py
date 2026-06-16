import streamlit as st

st.set_page_config(page_title="Contract Admin Tool", layout="wide")

st.title("Contract Administration Tool")

st.write("""
Use this tool to create, check and issue employment contracts.

Workflow:
1. Enter employee details
2. Select employment type and award
3. Check minimum compliance
4. Generate contract
5. Approve and issue
""")
