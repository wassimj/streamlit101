import streamlit as st
from topologicpy.Cell import Cell
from topologicpy.Plotly import Plotly

st.title('🎈 TopologicPy is on Streamlit!')

torus = Cell.Torus()
data = Plotly.DataByTopology(torus)
fig = Plotly.FigureByData(data)
st.plotly_chart(fig)

