"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import altair as alt
from cif import cif

data, subjects, measures = cif.createOneCountryDataFrameFromOECD(country= 'ESP', dsname='MEI')

st.write("### Subjects ", subjects.sort_index())

ipc = data['CPHP0702']['IXOB'].reset_index()

ipc_chart = (alt.Chart(ipc)
        .mark_area(opacity=0.3)
        .encode(
            x="time:T",
            y=alt.Y("IXOB:Q", stack=None),
            color="Region:N",
        )
)
st.altair_chart(ipc_chart, use_container_width=True)

st.line_chart(data=ipc, x = 'time', y = 'IXOB', use_container_width=True)