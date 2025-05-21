from utils import StockAPI
import streamlit as st

# Initialize the web app
st.set_page_config(page_title="Stock Market Project", layout="wide")

# Import the stock api client
client = StockAPI()

# Add a title to webpage
st.title("Stock Market Project")

# Add author name as subheader
st.subheader("by Himani Nathwani")

# Add company name as input
company = st.text_input("Company Name")

# If company name is input then
if company:
    search = client.symbol_search(company)
    options = st.selectbox("Company Symbol", options=search.keys())
    