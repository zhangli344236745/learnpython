import numpy as np
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file = st.file_uploader("upload a file",type="csv")

if st.button("get data"):
    df = pd.read_csv(file)
    st.write(df)

if st.button('save'):
    df.to_csv('data.csv')

x = np.linspace(0,10,100)
y = np.sin(x)

fig,ax = plt.subplots()
ax.plot(x,y)
st.write(fig)

code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')

df2 = pd.DataFrame(
    np.random.rand(50,20),
    columns=("col %d" % i for i in range(20)),
)

st.dataframe(df2.style.highlight_max(axis=1))