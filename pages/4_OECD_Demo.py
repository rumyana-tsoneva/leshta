"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import altair as alt

df = pd.DataFrame({
  'A': [1, 2, 3, 4],
  'B': [10, 20, 30, 40]
})
chart = (alt.Chart(df)
        .mark_area(opacity=0.3)
        .encode(
            x="A:T",
            y=alt.Y("B:Q", stack=None),
            color="Region:N",
        )
)
st.altair_chart(chart, use_container_width=True)