# Business Dashboard

This project is a Streamlit-based business dashboard for analyzing sales data from a superstore dataset. It provides interactive visualizations and key performance indicators (KPIs) to help stakeholders make data-driven decisions.

## Features

- **Interactive Dashboard**: Built with Streamlit for easy web-based access.
- **Data Visualization**: Uses Plotly for dynamic charts including bar charts, pie charts, and line graphs.
- **Filtering Options**: Filter data by region, category, and year range.
- **Key Metrics**: Displays total sales, total profit, and average profit margin.
- **Time Series Analysis**: Shows sales trends over time.
- **Top Products and Sub-Category Insights**: Highlights top-performing products and profit by sub-category.

## Files

- `app.py`: Main Streamlit application file containing the dashboard logic.
- `superstore.csv`: Sample dataset containing sales data.
- `create_ppt.py`: Script for generating PowerPoint presentations (if applicable).
- `dashboard_summary.pptx`: PowerPoint file with dashboard summaries.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/3407Naveen/task4.git
   cd task4
   ```

2. Install the required dependencies:
   ```
   pip install streamlit pandas plotly
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the provided local URL (usually `http://localhost:8501`).

3. Use the sidebar filters to customize the data view.

## Data Source

The dashboard uses a sample superstore dataset (`superstore.csv`) containing information about orders, customers, products, and sales metrics.

## Contributing

Feel free to fork this repository and submit pull requests for improvements or additional features.

## License

This project is open-source and available under the [MIT License](LICENSE).
