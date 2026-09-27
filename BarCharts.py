import pandas as pd
import altair as alt

cars_data=pd.read_csv("Datasets/car_price_data.csv")

alt.renderers.enable('browser')

chart1=alt.Chart(cars_data,height=400,width=600).mark_bar().encode(x="carbody",y="median(price)")
chart1.show()

#data value show
bar_chart=alt.Chart(cars_data,height=400,width=600).mark_bar().encode(x=alt.X("carbody",sort="y"),y="median(horsepower):Q")
text=bar_chart.mark_text(dy=-5).encode(text="median(horsepower):Q")
(bar_chart+text).show()


colorful_bar=alt.Chart(cars_data,height=400,width=600).mark_bar().encode(x="CarName",y="price",color=alt.condition(alt.datum.price>18000,alt.value("pink"),alt.value("steelblue")))
colorful_bar.show()

#draw line
hor_bar=alt.Chart(cars_data,height=400,width=600).mark_bar().encode(y="CarName",x="price",color=alt.condition(alt.datum.price>18000,alt.value("pink"),alt.value("steelblue")))
rule=alt.Chart(cars_data).mark_rule(color="red").encode(x="median(price):Q")
(hor_bar+rule).show()

stacked_bar=alt.Chart(cars_data,height=400,width=300).mark_bar().encode(y="carbody:O",x="count():Q",column="fueltype:O",color="drivewheel:N")
stacked_bar.show()

stacked_bar2=alt.Chart(cars_data,height=400,width=300).mark_bar().encode(x="carbody:O",y=alt.Y("count():Q",stack=None),column="fueltype:O",color="drivewheel:N")
stacked_bar2.show()