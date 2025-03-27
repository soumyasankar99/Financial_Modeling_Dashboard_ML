import streamlit as st
from loader import load_data
from data_preprocessing import preprocess_data, show_kpis
from data_visualization import show_visualizations
from data_forecasting import arima_forecasting, lstm_forecasting

st.set_page_config(page_title="Financial Dashboard", layout="wide")
st.title("💰 Financial Modeling Dashboard")

uploaded_file = st.file_uploader("Upload CSV, Excel or TSV", type=['csv', 'xls', 'xlsx', 'tsv'])

if uploaded_file:
    df = load_data(uploaded_file)

    if df is not None:
        st.subheader("📄 Raw Data")
        st.dataframe(df.head())

        df = preprocess_data(df)
        show_kpis(df, st)
        show_visualizations(df, st)
        arima_forecasting(df, st)
        lstm_forecasting(df, st)

        st.download_button("📥 Download Processed Data", df.to_csv().encode(), "processed_data.csv")

    else:
        st.error("🚫 Unsupported file type or load error.")
else:
    st.info("📂 Please upload a data file to start.")
