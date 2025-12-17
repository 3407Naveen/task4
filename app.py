import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Business Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for consistent theme
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 0.5rem 0;
    }
    .sidebar-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('superstore.csv')
    df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    return df

df = load_data()

# Sidebar navigation
st.sidebar.markdown('<div class="sidebar-header">📊 Business Dashboard</div>', unsafe_allow_html=True)

# Filters
st.sidebar.markdown("### Filters")
regions = st.sidebar.multiselect("Select Regions", options=df['Region'].unique(), default=df['Region'].unique())
categories = st.sidebar.multiselect("Select Categories", options=df['Category'].unique(), default=df['Category'].unique())
years = st.sidebar.slider("Select Year Range", min_value=int(df['Year'].min()), max_value=int(df['Year'].max()), value=(int(df['Year'].min()), int(df['Year'].max())))

# Filter data
filtered_df = df[
    (df['Region'].isin(regions)) &
    (df['Category'].isin(categories)) &
    (df['Year'].between(years[0], years[1]))
]

# Main content
st.markdown('<div class="main-header">Business Performance Dashboard</div>', unsafe_allow_html=True)

# KPIs
col1, col2, col3 = st.columns(3)

with col1:
    total_sales = filtered_df['Sales'].sum()
    st.markdown(f"""
    <div class="metric-card">
        <h3>Total Sales</h3>
        <h2>${total_sales:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)

with col2:
    total_profit = filtered_df['Profit'].sum()
    st.markdown(f"""
    <div class="metric-card">
        <h3>Total Profit</h3>
        <h2>${total_profit:,.2f}</h2>
    </div>
    """, unsafe_allow_html=True)

with col3:
    avg_growth = (filtered_df['Profit'] / filtered_df['Sales']).mean() * 100 if filtered_df['Sales'].sum() > 0 else 0
    st.markdown(f"""
    <div class="metric-card">
        <h3>Average Profit Margin</h3>
        <h2>{avg_growth:.2f}%</h2>
    </div>
    """, unsafe_allow_html=True)

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Category")
    category_sales = filtered_df.groupby('Category')['Sales'].sum().reset_index()
    fig_category = px.bar(category_sales, x='Category', y='Sales', color='Category',
                          color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c'])
    fig_category.update_layout(showlegend=False)
    st.plotly_chart(fig_category, use_container_width=True)

with col2:
    st.subheader("Sales by Region")
    region_sales = filtered_df.groupby('Region')['Sales'].sum().reset_index()
    fig_region = px.pie(region_sales, values='Sales', names='Region',
                        color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    st.plotly_chart(fig_region, use_container_width=True)

# Time series analysis
st.subheader("Sales Trend Over Time")
monthly_sales = filtered_df.groupby(['Year', 'Month'])['Sales'].sum().reset_index()
monthly_sales['Date'] = pd.to_datetime(monthly_sales[['Year', 'Month']].assign(DAY=1))
monthly_sales = monthly_sales.sort_values('Date')

fig_time = px.line(monthly_sales, x='Date', y='Sales', markers=True,
                   color_discrete_sequence=['#1f77b4'])
fig_time.update_layout(xaxis_title="Date", yaxis_title="Sales")
st.plotly_chart(fig_time, use_container_width=True)

# Additional insights
col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 5 Products by Sales")
    top_products = filtered_df.groupby('Product Name')['Sales'].sum().nlargest(5).reset_index()
    fig_products = px.bar(top_products, x='Sales', y='Product Name', orientation='h',
                          color_discrete_sequence=['#1f77b4'])
    fig_products.update_layout(yaxis={'categoryorder':'total ascending'})
    st.plotly_chart(fig_products, use_container_width=True)

with col2:
    st.subheader("Profit by Sub-Category")
    subcategory_profit = filtered_df.groupby('Sub-Category')['Profit'].sum().reset_index()
    fig_subcategory = px.bar(subcategory_profit, x='Sub-Category', y='Profit',
                             color='Profit', color_continuous_scale='Blues')
    fig_subcategory.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_subcategory, use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Dashboard created for business stakeholders to inform data-driven decisions.")
