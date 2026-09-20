import streamlit as st
import main

st.set_page_config(page_title="Tracker Pro", page_icon="🚀")
st.title("🚀 Tracker Pro is ON")

if hasattr(main, 'run'):
    main.run()
else:
    st.success("Pro Loaded! main.py connected")
    