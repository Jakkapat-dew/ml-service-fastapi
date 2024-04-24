import streamlit as st
import requests
from io import StringIO

st.set_page_config(
    page_title="ML App demo",
    layout="wide"
)

ML_API_URL = 'http://127.0.0.1:8000/'
ML_API_URL_READ_CSV = ML_API_URL + 'dataGetting/read_csv/'

uploaded_csvfile = st.file_uploader("Choose a CSV file", type=['csv'])
# To convert to a string based IO:
stringio = StringIO(uploaded_csvfile.getvalue().decode("utf-8"))

print(stringio)

data_from_csv = requests.post(url=ML_API_URL_READ_CSV, files=stringio)
    
st.write(data_from_csv)