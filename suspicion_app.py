import streamlit as st
import pickle
import pandas as pd

# Load model
model = pickle.load(open('tree_model.sav', 'rb'))

st.set_page_config(page_title="Fake Suspicion App")
st.title("Fake Suspicion App")
st.write("Input values and get suspicion prediction for the architype")

# User input
st.text_input("Is vrouw:", key="vrouw", value="0")
st.text_input("Aantal huisgenoten:", key="huisgenoten", value="0")
st.text_input("Leeftijd:", key="leeftijd", value="55")
st.text_input("Financiele problemen:", key="fin_prob", value="0")
st.text_input("Energieverbruik:", key="energieverbruik", value="360")
st.text_input("Pintransacties buiten wijk:", key="pin_buiten_wijk", value="0")
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

# Predict button
# if st.button("Analyze"):
#     if message:
#         prediction = model.predict([message])[0]
#         label = "🚫 Spam" if prediction else "✅ Not Spam"
#         st.success(f"Prediction: {label}")
#     else:
#         st.warning("Please enter a message.")