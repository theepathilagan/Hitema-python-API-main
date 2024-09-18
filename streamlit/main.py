import streamlit as st
import numpy as np
import pandas as pd

def load_data():
    data = pd.read_csv("dataset.csv")
    return data

st.title("Speed Test Analytics")

if st.checkbox("Afficher les données"):
    st.subheader("Dataset SpeedTest by Oakala")
    st.write(load_data())

