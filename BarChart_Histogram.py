import altair as alt
import pandas as pd

alt.renderers.enable('browser')

car_datas=pd.read_csv("Datasets/car_price_data.csv")

chart1=alt.Chart(car_datas).mark_bar().encode(x="horsepower", y="count()").properties(width=600)

#histogram
chart2=alt.Chart(car_datas).mark_bar().encode(x=alt.X("horsepower:Q",bin=True),y="count()").properties(width=600)

#histogram with max bin
chart3=alt.Chart(car_datas).mark_bar().encode(x=alt.X("horsepower:Q",bin=alt.BinParams(maxbins=3)),y="count()").properties(width=600)

#chart4 chart2 same
chart4=alt.Chart(car_datas).transform_fold(["horsepower"]).mark_bar().encode(x=alt.X("value:Q",bin=True),y="count()").properties(width=600)

chart5=alt.Chart(car_datas).transform_fold(fold=["horsepower","enginesize"],as_=["Car Property","value"]).mark_bar(opacity=0.4).encode(
                                                                                                                                        alt.X("value:Q",bin=alt.BinParams(maxbins=10)),
                                                                                                                                        alt.Y("count()",stack=None),
                                                                                                                                              alt.Color("Car Property:N")).properties(width=600)
#chart1.show()
#chart2.show()
#chart3.show()
#chart4.show()
chart5.show()

