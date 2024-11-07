from streamlit_gsheets import GSheetsConnection
import streamlit as st

def db_conn():
    conn = st.connection("gsheets", type=GSheetsConnection)
    return conn







