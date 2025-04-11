import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

st.title("Advanced Data Dashboard")

uploaded_file = st.file_uploader("Upload a file (CSV, Excel, JSON, Image)", type=["csv", "xlsx", "xls", "json", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    file_type = uploaded_file.name.split(".")[-1]
    
    if file_type == "csv":
        df = pd.read_csv(uploaded_file)
    elif file_type in ["xlsx", "xls"]:
        df = pd.read_excel(uploaded_file)
    elif file_type == "json":
        df = pd.read_json(uploaded_file)
    elif file_type in ["png", "jpg", "jpeg"]:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.write("Image uploaded successfully.")
        st.stop()
    else:
        st.error("Unsupported file format")
        st.stop()
    
    st.subheader("Data Preview")
    st.write(df.head())
    
    st.subheader("Data Summary")
    st.write(df.describe())
    
    st.subheader("Filter Data")
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)
    unique_values = df[selected_column].dropna().unique()
    selected_value = st.selectbox("Select value", unique_values)
    
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)
    
    st.subheader("Plot Data")
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)
    chart_type = st.selectbox("Select chart type", ["Line", "Bar", "Scatter"])
    
    if st.button("Generate Plot"):
        fig, ax = plt.subplots()
        if chart_type == "Line":
            ax.plot(filtered_df[x_column], filtered_df[y_column], marker='o')
        elif chart_type == "Bar":
            ax.bar(filtered_df[x_column], filtered_df[y_column])
        elif chart_type == "Scatter":
            ax.scatter(filtered_df[x_column], filtered_df[y_column])
        
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        ax.set_title(f"{chart_type} Plot of {y_column} vs {x_column}")
        st.pyplot(fig)
else:
    st.write("Waiting for file upload...")
