import streamlit as st
from PIL import Image
import base64
import streamlit as st
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image_file.jpeg')  

def main():
    # Create a banner at the top with links to other pages
    with st.container():
        st.markdown(
            """
            <div style='background-color: white; padding: 1px;'>
            <h1 style='font-family:Optima;color: #8B4513; text-align: center;'>Jorge & Jeff</h1>
            <p style='font-family: Optima;color: #8B4513; text-align: center; font-size: 20px;'> 
            <a style='color: #8B4513; text-decoration: none;' href='/'>Homepage</a> | 
            <a style='color: #8B4513; text-decoration: none;' href='/clothing'>Clothing</a> | 
            <a style='color: #8B4513; text-decoration: none;' href='/about'>About</a> | 
            <a style='color: #8B4513; text-decoration: none;' href='https://georginapalmer-teampage-teampage-1k7d1b.streamlit.app' target='_blank'>Team</a>
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )
if __name__ == '__main__':
     main()
# Create two columns
col1, col2 = st.columns(2)

# Display images and labels in the first column
with col1:
    Ewan_title = '<strong><p style="font-family:Optima; color:#8B4513; font-size: 23px;">Ewan Yeo</p></strong>'
    st.markdown(Ewan_title, unsafe_allow_html=True)
    roleewan_title = '<p style="font-family:Optima; color:#8B4513; font-size: 20px;">Jorge Santos, Co-Founder</p>'
    st.markdown(roleewan_title, unsafe_allow_html=True)
    image3 = Image.open('Ewan.jpeg')
    st.image(image3, width=300)
    
    Charlotte_title = '<strong><p style="font-family:Optima; color:#8B4513; font-size: 23px;">Charlotte Guillemot</p></strong>'
    st.markdown(Charlotte_title, unsafe_allow_html=True)
    rolecharlotte_title = '<p style="font-family:Optima; color:#8B4513; font-size: 20px;">Creative Director</p>'
    st.markdown(rolecharlotte_title, unsafe_allow_html=True)
    image6 = Image.open('Charlotte.jpeg')
    st.image(image6, width=300)
    
    Ethan_title = '<strong><p style="font-family:Optima; color:#8B4513; font-size: 23px;">Ethan Woolley</p></strong>'
    st.markdown(Ethan_title, unsafe_allow_html=True)
    roleethan_title = '<p style="font-family:Optima; color:#8B4513; font-size: 20px;">CTO</p>'
    st.markdown(roleethan_title, unsafe_allow_html=True)
    image5 = Image.open('Ethan.jpeg')
    st.image(image5, width=300)


# Display images and labels in the second column
with col2:
    Rajat_title = '<strong><p style="font-family:Optima; color:#8B4513; font-size: 23px;">Rajat Khole</p></strong>'
    st.markdown(Rajat_title, unsafe_allow_html=True)
    rolerajat_title = '<p style="font-family:Optima; color:#8B4513; font-size: 20px;">Jeff Bridges, Co-Founder</p>'
    st.markdown(rolerajat_title, unsafe_allow_html=True)
    image4 = Image.open('Rajat.jpeg')
    st.image(image4, width=300)

    Georgina_title = '<strong><p style="font-family:Optima; color:#8B4513; font-size: 23px;">Georgina Palmer</p></strong>'
    st.markdown(Georgina_title, unsafe_allow_html=True)
    rolegeorgina_title = '<p style="font-family:Optima; color:#8B4513; font-size: 20px;">CFO </p>'
    st.markdown(rolegeorgina_title, unsafe_allow_html=True)
    image7 = Image.open('Georgie.jpeg')
    st.image(image7, width= 300)

    Logo_title = '<strong><p style="font-family:Optima; color:#8B4513; font-size: 20px;"> ChatGPT </p></strong>'
    st.markdown(Logo_title, unsafe_allow_html=True)
    gpt_title = '<p style="font-family:Optima; color:#8B4513; font-size: 20px;"> Strategic Advisor </p>'
    st.markdown(gpt_title, unsafe_allow_html=True)
    imLogo = Image.open('chatgpt.jpeg')
    st.image(imLogo, width = 300)
    

    