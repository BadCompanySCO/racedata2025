import streamlit as st
import pandas as pd
import openpyxl as opxl
import plotly.express as px  # pip install plotly-express



st.title("🎈 We Run Scotland ")
st.write(
    "Upload Race Data"
)

# File uploader widget
uploaded_file = st.file_uploader("Choose an XLSX file", type=["xlsx"])

if uploaded_file is not None:
    # Read the Excel file into a pandas DataFrame
    try:
        df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error reading the file: {e}")
        df = None

    if df is not None:
        # Display the DataFrame
        st.dataframe(df)

        # Optional: Add more functionalities here
        # For example:
        # - Display summary statistics
        # - Allow users to filter or sort the data
        # - Create visualizations
