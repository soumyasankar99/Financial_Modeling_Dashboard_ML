import pandas as pd

def preprocess_data(df):
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

    df = df.sort_values('Date')
    df.set_index('Date', inplace=True)
    df['Profit'] = df['Revenue'] - df['Expense']
    df['Gross Profit Margin'] = (df['Profit'] / df['Revenue']) * 100
    df['Expense Ratio'] = (df['Expense'] / df['Revenue']) * 100
    return df

def show_kpis(df, st):
    st.subheader("📌 Key Performance Indicators")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", f"${df['Revenue'].sum():,.2f}")
    col2.metric("Total Expense", f"${df['Expense'].sum():,.2f}")
    col3.metric("Total Profit", f"${df['Profit'].sum():,.2f}")
    st.metric("Avg Gross Profit Margin", f"{df['Gross Profit Margin'].mean():.2f}%")
    st.metric("Avg Expense Ratio", f"{df['Expense Ratio'].mean():.2f}%")
