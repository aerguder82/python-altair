import encodings

import altair as alt
import pandas as pd

alt.renderers.enable('browser')
weather_data=pd.read_csv("Datasets/sydney_weather.csv",parse_dates=["Date"],dayfirst=True)

chart1=alt.Chart(weather_data,height=400,width=600).mark_line().encode(x="Date:T",y="MaxTemp:O")
chart1.show()

weather_jan=weather_data[weather_data["Date"]<pd.Timestamp(2016,2,1)]   #filtered data

#zoom
full_year_maxtemp=alt.Chart(weather_data,height=400,width=600).mark_line(interpolate="basis").encode(x="Date:T",y="MaxTemp:O")
brush=alt.selection(type="interval", encodings=["x"])
main_chart=full_year_maxtemp.encode(alt.X("Date:T",scale=alt.Scale(domain=brush)))
control_chart=full_year_maxtemp.properties(height=100).add_selection(brush)
(main_chart & control_chart).show()

multi_chart=alt.Chart(weather_jan,height=400,width=600).transform_fold(fold=["MinTemp","MaxTemp"],as_=["Temperature Type","value"]).mark_line(interpolate="basis").encode(x="Date:T",y="value:Q",color="Temperature Type:O",strokeDash="Temperature Type:O")
multi_chart.show()

