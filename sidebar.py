import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Belajar Analisis Data')
tab1, tab2, tab3, tab4= st.tabs(["Tab 1", "Tab 2", "Tab 3", "Container"])

with st.sidebar:
    st.text('Ini merupakan sidebar')
    values = st.slider(
        label = 'Select a range of values',
        min_value = 0, max_value = 100, value = (0, 100)
    )
    st.write('Selected range:', values)

with tab1:
    st.header('Tab 1')
    st.image("https://static.streamlit.io/examples/cat.jpg")

with tab2:
    st.header("Tab 2")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with tab3:
    st.header("Tab 3")
    st.image("https://static.streamlit.io/examples/owl.jpg")

with tab4:
    with st.container():
        st.write("Inside the container")
    
        x = np.random.normal(15, 5, 250)

        fig, ax = plt.subplots()
        ax.hist(x=x, bins=15)
        st.pyplot(fig)

st.write("Outside the container")