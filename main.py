import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.title('Dynamic pressure profile')
st.sidebar.title('inputs')
p=float
B=float
k=st.sidebar.slider('permeability(md)', min_value=10,max_value=100,value=100)
mu=st.sidebar.slider('viscosity(u)', min_value=10,max_value=200,value=100)
q=st.sidebar.slider('flowrate(STB/DAY)', min_value=10,max_value=2000,value=200)
re=st.sidebar._number_input('OUTER RADIUS(FT)',min_value=1000,max_value=10000,value=3000)
rw=st.sidebar.number_input('WELL BORE RADIUS(FT)',min_value=1,max_value=10,value=1)
pe=st.sidebar.number_input('pressure at boundary of reservoir(psi)',min_value=100,max_value=10000,value=4000)
B=st.sidebar.number_input('FORMATION VOLUME FACTOR(bbl/stb)',min_value=1,max_value=2,value=1)
h=st.sidebar.number_input('net pay thickness of reservoir(feet)',min_value=2,max_value=500,value=30)
r = np.linspace(rw,re,500)
p=pe - (141.2*q*mu*B*(np.log(re/r))/k/h)
y_min=p[np.where(r==rw)]
b=st.button('show reservoir profile')
if b:
    plt.style.use('classic')
    plt.figure(figsize=(8,6))
    fig,ax=plt.subplots()
    ax.plot(r,p,linewidth=4)
    ax.grid(True)
    ax.axhline(y_min,linewidth=3,color='red')
    ax.set_xlabel("radius(feet)")
    ax.set_ylabel("pressure at radius r,(psi)")
    ax.set_title('pressure profile')
    ax.set_ylim(0,5000)
    st.pyplot(fig)