import streamlit as st
from topologicpy.Cell import Cell
from topologicpy.Topology import Topology
from topologicpy.Plotly import Plotly

st.title('🎈 TopologicPy is on Streamlit!')

torus = Cell.Torus()
cluster = Topology.Explode(torus)
data = Plotly.DataByTopology(cluster)
fig = Plotly.FigureByData(data)
st.plotly_chart(fig)

