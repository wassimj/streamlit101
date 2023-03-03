import streamlit as st
import topologicpy
from topologicpy.Cell import Cell
from topologicpy.Plotly import Plotly

st.title('🎈 TopologicPy is on PyPI!')

torus = Cell.Torus()
data = Plotly.DataByTopology(torus)
fig = Plotly.FigureByData(data)
st.plotly_chart(fig)

