import altair as alt
import pandas as pd
from dateutil.utils import within_delta

alt.renderers.enable('browser')

utahnp_data=pd.read_csv("Datasets/utah_np_2019.csv")

chart1=alt.Chart(utahnp_data,width=600,height=400).mark_area(color="green",opacity=0.4, line={"color":"darkgreen"}).encode(x="Month:N",y="Zion:Q")
chart1.show()

#chart2 gradient color
chart2=alt.Chart(utahnp_data,width=600,height=400).mark_area(opacity=0.4,
                                                             line={"color":"darkgreen"},
                                                             color=alt.Gradient(gradient="linear",
                                                                                stops=[alt.GradientStop(color="red",offset=0),
                                                                                       alt.GradientStop(color="green",offset=1)],
                                                                                x1=1,
                                                                                x2=1,
                                                                                y1=1,
                                                                                y2=0
                                                                                )
                                                             ).encode(x="Month:N",
                                                                      y="Zion:Q")
chart2.show()


