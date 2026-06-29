import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open('tree_model.sav', 'rb'))

st.set_page_config(page_title="Fake Suspicion App")
st.title("Fake Suspicion App")
'''
*Input values and get suspicion prediction for the architype*

The model behind this app is completely fake and not based on the Lighthouse dataset nor does it reflect real world scenarios in the city of Rotterdam.
'''

# User input
CHOICES_GESLACHT = {0: "Man", 1: "Vrouw"}
def format_func_geslacht(option):
    return CHOICES_GESLACHT[option]
st.selectbox("Geslacht:", options=list(CHOICES_GESLACHT.keys()), format_func=format_func_geslacht, key="vrouw", index=0)
st.text_input("Aantal huisgenoten:", key="huisgenoten", value="0")
st.text_input("Leeftijd:", key="leeftijd", value="55")
CHOICES_FIN = {1: "Ja", 0: "Nee"}
def format_func_fin(option):
    return CHOICES_FIN[option]
st.selectbox("Financiele problemen:", options=list(CHOICES_FIN.keys()), format_func=format_func_fin, key="fin_prob", index=0)
st.text_input("Energieverbruik:", key="energieverbruik", value="360")
CHOICES_PIN = {1: "Ja", 0: "Nee"}
def format_func_pin(option):
    return CHOICES_PIN[option]
st.selectbox("Pintransacties buiten wijk:", options=list(CHOICES_PIN.keys()), format_func=format_func_pin, key="pin_buiten_wijk", index=0)
st.text_input("Aantal pintransacties:", key="pintransacties", value="48")
st.text_input("Aantal wijzigingen:", key="wijzigingen", value="21")
st.text_input("Aantal autos:", key="autos", value="1")

input_dict = {'vrouw': st.session_state.vrouw,
              'huisgenoten': st.session_state.huisgenoten,
              'leeftijd': st.session_state.leeftijd,
              'fin_prob': st.session_state.fin_prob,
              'energieverbruik': st.session_state.energieverbruik,
              'pin_buiten_wijk': st.session_state.pin_buiten_wijk,
              'pintransacties': st.session_state.pintransacties,
              'wijzigingen': st.session_state.wijzigingen,
              'autos': st.session_state.autos}

test_input = pd.DataFrame([input_dict])

if st.button("Analyze"):
    prediction = model.predict(test_input)
    label = "Suspicion Score: " + str(prediction)
    st.success(f"Prediction: {label}")
    # st.write(f"Financiële problemen: {st.session_state.fin_prob} en formatted: {format_func_fin(st.session_state.fin_prob)}")

# Predict button
# if st.button("Analyze"):
#     if message:
#         prediction = model.predict([message])[0]
#         label = "🚫 Spam" if prediction else "✅ Not Spam"
#         st.success(f"Prediction: {label}")
#     else:
#         st.warning("Please enter a message.")