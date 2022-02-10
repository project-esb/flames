import streamlit as st

def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url("https://pixabay.com/images/id-3061483/");
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
st.markdown('<center><h1>🅵🅻🅰🅼🅴🆂</h1></center>',unsafe_allow_html=True)
set_bg_hack_url()






