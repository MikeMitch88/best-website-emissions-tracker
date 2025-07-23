import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="GreenShift - Carbon Footprint Tracker",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.logo("Images/menu.png")

# --- Buy Me A Coffee Button (Global, top right) ---
st.markdown(
    """
    <div style="text-align:right; margin-top:-30px; margin-bottom:10px;">
        <a href="https://www.buymeacoffee.com/michaelranda" target="_blank">
            <img src="https://www.buymeacoffee.com/assets/img/guidelines/download-assets-sm-1.svg" alt="Buy Us Coffee" style="height: 60px;" />
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

pages = {
    "App Navigations": [
        st.Page("home.py", title="Home", icon='🏠' ,default=True),
        st.Page("developers.py", title="Developers | Team", icon='👨‍🏫'),
    ],
    "Modules": [
        st.Page("user_input.py", title="Calculate My Carbon Footprint", icon='🐾'),
        st.Page("recommendations.py", title="Recommendations",  icon='🤹‍♂️'),
        st.Page("Global_Climate.py", title="Global Carbon Emission",  icon='🏭'),
        st.Page("sustainability.py", title="Sustainable Practices",  icon='🌱')
    ]
}

pg = st.navigation(pages)
pg.run()

