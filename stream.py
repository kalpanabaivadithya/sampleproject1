import ai_chatbot as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Page settings
st.set_page_config(page_title="Smart Data Analyzer", layout="wide")

# Title
st.title("📊 Smart Data Analyzer Dashboard")

# File Upload
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    
    # Read file
    data = pd.read_csv(uploaded_file)

    # Show dataset
    st.subheader("Dataset Preview")
    st.dataframe(data)

    # Shape
    st.write("Rows and Columns:", data.shape)

    # Missing values
    st.subheader("Missing Values")
    st.write(data.isnull().sum())

    # Remove duplicates
    if st.button("Remove Duplicate Rows"):
        data = data.drop_duplicates()
        st.success("Duplicates Removed Successfully")

    # Column selection
    st.subheader("Select Columns")
    selected_columns = st.multiselect(
        "Choose Columns",
        data.columns,
        default=data.columns
    )

    filtered_data = data[selected_columns]
    st.dataframe(filtered_data)

    numeric_cols = filtered_data.select_dtypes(include=np.number).columns

    # Chart options
    st.subheader("Visualization")

    chart_option = st.selectbox(
        "Choose Chart Type",
        ["Bar Chart", "Line Chart", "Histogram", "Scatter Plot", "Heatmap"]
    )

    if len(numeric_cols) > 0:

        if chart_option == "Bar Chart":
            st.bar_chart(filtered_data[numeric_cols])

        elif chart_option == "Line Chart":
            st.line_chart(filtered_data[numeric_cols])

        elif chart_option == "Histogram":
            col = st.selectbox("Select Column", numeric_cols)

            fig, ax = plt.subplots()
            ax.hist(filtered_data[col], bins=10)
            ax.set_title("Histogram")
            st.pyplot(fig)

        elif chart_option == "Scatter Plot":
            x_col = st.selectbox("Select X Column", numeric_cols)
            y_col = st.selectbox("Select Y Column", numeric_cols)

            fig, ax = plt.subplots()
            ax.scatter(filtered_data[x_col], filtered_data[y_col])
            ax.set_xlabel(x_col)
            ax.set_ylabel(y_col)
            st.pyplot(fig)

        elif chart_option == "Heatmap":
            fig, ax = plt.subplots(figsize=(8,5))
            sns.heatmap(filtered_data[numeric_cols].corr(), annot=True, ax=ax)
            st.pyplot(fig)

    else:
        st.error("No numeric columns found!")

    # Statistics
    st.subheader("Statistical Summary")
    st.write(filtered_data.describe())

    # Download cleaned file
    csv = filtered_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Cleaned Dataset",
        data=csv,
        file_name="cleaned_data.csv",
        mime="text/csv"
    )

else:
    st.info("Please upload a CSV file to begin analysis.")