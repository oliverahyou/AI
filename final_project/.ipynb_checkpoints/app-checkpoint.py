import streamlit as st
import pandas as pd
import plotly.express as px

# Configure wide layout layout
st.set_page_config(layout="wide", page_title="Coffee Audience Analytics")
st.title("☕ Coffee Brands A & B: Target Audience Breakdown")

# 1. File Uploader Widget
uploaded_file = st.file_uploader("Upload your Coffee Dataset (CSV)", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Precise, exact lowercase column checklist
    required_columns = ['id', 'gender', 'age', 'brand', 'feedback']
    
    # Strict validation check
    if not all(col in df.columns for col in required_columns):
        st.error(f"Error: Dataset must contain these exact lowercase columns: {required_columns}")
        st.stop()

    # 2. Sidebar control panel
    st.sidebar.header("🎯 Dashboard Settings")
    selected_brands = st.sidebar.multiselect(
        "Compare Brands:", 
        options=df['brand'].unique(), 
        default=df['brand'].unique()
    )
    
    # Filter dataset matching selection
    filtered_df = df[df['brand'].isin(selected_brands)]

    # 3. Layout Grid for Metrics and Overview Charts
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("👥 Age Demographics by Brand")
        # Aggregating rows using lowercase column names
        age_brand_data = filtered_df.groupby(['age', 'brand']).size().reset_index(name='count')
        
        fig_age = px.bar(
            age_brand_data, 
            x='age', 
            y='count', 
            color='brand', 
            barmode='group',
            labels={'age': 'Age Group', 'count': 'Customer Count'},
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_age, use_container_width=True)

    with col2:
        st.subheader("🚺🚹 Gender Proportions per Brand")
        # Aggregating gender metrics 
        gender_brand_data = filtered_df.groupby(['gender', 'brand']).size().reset_index(name='count')
        
        fig_gender = px.bar(
            gender_brand_data, 
            x='brand', 
            y='count', 
            color='gender', 
            barmode='stack',
            labels={'brand': 'Brand Group', 'count': 'Total Responses'},
            color_discrete_sequence=px.colors.qualitative.Safe
        )
        st.plotly_chart(fig_gender, use_container_width=True)

    # 4. Multi-level Audience Breakdown Map
    st.markdown("---")
    st.subheader("🗺️ Demographic Segmentation Tree")
    
    fig_tree = px.treemap(
        filtered_df, 
        path=['brand', 'gender', 'age'], 
        color='brand',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig_tree, use_container_width=True)

    # 5. Ordered Data Viewer
    st.markdown("---")
    st.subheader("💬 Raw Customer Responses")
    
    # Display columns in the requested sequence
    ordered_display_df = filtered_df[required_columns]
    st.dataframe(ordered_display_df, use_container_width=True)

else:
    st.info("💡 Please upload your CSV file containing columns: id, gender, age, brand, feedback")