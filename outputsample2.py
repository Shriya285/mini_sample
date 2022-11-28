import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(layout="wide")
import streamlit as st

st.markdown("""
<style>
.big-font {
    font-size:50px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Job Coach</p>', unsafe_allow_html=True)


tab1, tab2, tab3 = st.tabs(["Personal Information","Application Form","Your Jobs"])
with tab3:
    
        st.title("Type of job:")
        a=st.checkbox("Internhip")
        b=st.checkbox("Part-Time")
        c=st.checkbox("Full-Time")
        if a:
            st.write("Internship")
        elif b:
            st.write("Part-Time")
        elif c:
            st.write("Full-Time")
        else:
            st.write(" ")
        
        st.title("Salary:")
        salary = st.slider(
    'Select Salary Range(in Lakhs):',
    0.0, 100.0, (25.0, 75.0))
        st.write('Salary:', salary)
        
        options = st.multiselect(
    'What is your prefered Location?',
    ('Place1', 'Place2', 'Place3', 'Place4'))
        st.write('You selected:', options)

        st.title("Domain and Skillset:")
        st.subheader("Domain:")
        domain = st.text_input('Domain:', ' ')
        st.write('Your chosen Domain:', domain)
        st.subheader("Skillset:")
        skillset=st.text_area(" ")
        st.write(skillset)
df = pd.DataFrame(
        columns=("Company","Salary","Location"))
st.dataframe(df)
st.title("About the Company")
abt=st.text(" ---------------abc------------ ")
st.subheader("Size of the company:")
size=st.text("50-200 employees")
st.subheader("College Alumni")
alumni=st.text("34")
st.subheader("Responsibilities:")
st.text("--------------def-----------")
st.subheader("Work Life & Culture:")
image= Image.open(r"C:\Users\Shriya Konduru\Downloads\google.jpg",'r')

st.image(image)
st.caption("Benefits of working in this company are;----------")
       
#(**Just for Try**)
# Using object notation
add_selectbox = st.sidebar.selectbox(
    "Preferred Language",
    ("lang1", "lang2", "lang3")
)

# Using "with" notation
#with st.sidebar:
   # add_radio = st.radio(
    #    "Choose a shipping method",
     #   ("Standard (5-15 days)", "Express (2-5 days)")
    #)

