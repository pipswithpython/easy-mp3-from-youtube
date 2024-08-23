import streamlit as st # type: ignore
import api.tools as flexin

st.set_page_config(
    page_title="MP3 from YouTube",
    page_icon="🔊",
    layout="centered",
    initial_sidebar_state="collapsed",
)

with st.form(key = "form", clear_on_submit=True):

    st.code("📹 Turn Youtube Videos Into MP3 Easily 🔊", language="python")
    
    url = st.text_input(label="url", key="url", label_visibility="collapsed",type="default", placeholder="🔗 url here")

    if st.form_submit_button(label="download", type="secondary", use_container_width=True):
        
        st.progress(value=100, text="loading")

        st.code(f"▶️ {flexin.Video(url).title().title()}")

        col1, col2 = st.columns(2)

        with col1:

            st.image(image=flexin.Video(url).thumbnail(), use_column_width=True)

        with col2:

            st.code(f"🧑‍💻 {flexin.Video(url).author()}")

            st.code(f"📊 {flexin.Video(url).views()} | 📅 {flexin.Video(url).date()}")
            
            st.progress(value=100, text="download completed")
            
            flexin.Video.moneTagAds()

            flexin.Video(url).download()

baseboard = """
    <center>© 2024 Flexin®️ - all rights reserved.</center>
"""

st.write(baseboard, unsafe_allow_html=True)
