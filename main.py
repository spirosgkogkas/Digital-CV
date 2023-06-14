import streamlit as st
from PIL import Image
from pathlib import Path

st.set_page_config("Digital CV | Spiros Gkogkas", "👨‍💻")

# --- PATH SETTINGS ---
curr_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = curr_dir / "css" / "style.css"
profil_pic = curr_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
DESCRIPTION = "Passionate Programmer and Aspiring Software Developer"
EMAIL = "spirosgkogkas1998@gmail.com"
PHONE = "(+30) 6987807633"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/spiros-gkogkas-0435651b4",
    "Github": "https://github.com/spirosgkogkas",
    "StackOverflow": "https://stackoverflow.com/users/13775432/spiros-gkogkas"
}
ATM_DESCRIPTION = """
    I developed a C++ ATM Simulation Application emulating an Automated Teller Machine. Users can perform banking operations with secure authentication, error handling, and cross-platform compatibility. Demonstrates proficiency in C++, OOP, and standard libraries.
"""
git = "https://github.com/spirosgkogkas/Bank"

with open(css_file, "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

col1, col2 = st.columns([1,2], gap="small")

with col1:
    img = Image.open(profil_pic)
    col1.image(img, width=200)

with col2:
    col2.title("Spiros Gkogkas")
    st.write(DESCRIPTION)
    with open("./assets/CV - Spiros Gkogkas.pdf", "rb") as f:
        cv = f.read()        
    st.download_button("📄 Download Resume", data=cv, file_name="SpirosGkogkasCV.pdf", mime="application/pdf")
    st.write(f":email: {EMAIL}")
    st.write(f":iphone: {PHONE}")

st.write("\n")
social_columns = st.columns(len(SOCIAL_MEDIA.items()))

for index, (k, val) in enumerate(SOCIAL_MEDIA.items()):
    social_columns[index].write(f"[{k}]({val})")
st.write("\n")
st.subheader("Experience")

col3, col4 = st.columns(2, gap="small")
with col3:
    # st.write(f"**ATM Simulator** ([Source Code]({git}))")
    st.write(f"**ATM Simulator** (<a href='{git}' class='myclass123' >Source Code</a>)", unsafe_allow_html=True)

    st.write(ATM_DESCRIPTION)
    # with open("C:/Users/spiro/Downloads/Malware Development II_ Process Injection.mp4", "rb") as f:
    #     video = f.read()
    # st.video(video, format="video/mp4")

# with col4:
#     st.write("**ATM Simulator**")
#     st.write(ATM_DESCRIPTION)
#     with open("C:/Users/spiro/Downloads/Malware Development II_ Process Injection.mp4", "rb") as f:
#         video = f.read()
#     st.video(video, format="video/mp4")
