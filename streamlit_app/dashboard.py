import streamlit as st
import json
from google.oauth2 import service_account
from google.cloud import bigquery

# Load Google credentials from Streamlit secrets
creds = st.secrets["GOOGLE_CREDENTIALS"]
credentials = service_account.Credentials.from_service_account_info(creds)

# Initialize BigQuery client with credentials
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

st.set_page_config(layout="wide")
st.title("🏏 IPL Match Performance Analyzer")
