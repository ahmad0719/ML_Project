
import streamlit as st
import joblib
import numpy as np

st.set_page_config(page_title="Fetal Health Predictor", layout="centered")

st.title("Fetal Health Classification System")
st.markdown("Predict fetal state based on CTG features")

model = joblib.load("best_model.pkl")

feature_names = [
"LB","AC","FM","UC","ASTV","MSTV","ALTV","MLTV","Width","Min",
"Max","Nmax","Nzeros","Mode","Mean","Median","Variance","Tendency","Mean_val","Feature20","Feature21"
]

inputs = []
for f in feature_names:
    val = st.slider(f, 0.0, 200.0, 0.0)
    inputs.append(val)

if st.button("Predict"):
    pred = model.predict([inputs])[0]
    if pred == 1:
        st.success("Normal")
    elif pred == 2:
        st.warning("Suspect")
    else:
        st.error("Pathologic")
