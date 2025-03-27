import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def show_visualizations(df, st):
    st.subheader("📊 Visualizations")

    with st.expander("📈 Monthly Revenue Trend"):
        monthly = df['Revenue'].resample('M').sum()
        st.line_chart(monthly)

    if 'Expense Category' in df.columns:
        with st.expander("🧾 Expense Distribution"):
            pie_data = df.groupby('Expense Category').sum()['Expense']
            fig, ax = plt.subplots()
            ax.pie(pie_data, labels=pie_data.index, autopct='%1.1f%%')
            st.pyplot(fig)

    with st.expander("📌 Correlation Heatmap"):
        fig, ax = plt.subplots()
        sns.heatmap(df.select_dtypes(include='number').corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
