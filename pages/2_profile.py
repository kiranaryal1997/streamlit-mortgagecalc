import streamlit as st
import numpy as np
import pandas as pd

st.write("# Profile Page")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

#check 4x4 data
# df = pd.DataFrame(
#     np.random.randn(4,4,),
#     columns = ["A", "B", "C", "D"]
# )

# st.write(df)

# st.write(chart_data)

st.bar_chart(chart_data)
st.line_chart(chart_data)