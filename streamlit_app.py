import streamlit as st
import topologicpy
from topologicpy.Cell import Cell
from topologicpy.Topology import Topology
from topologicpy.Plotly import Plotly

st.title('🎈 TopologicPy is on Streamlit!')

torus = Cell.Torus()
Topology.Show(torus)

