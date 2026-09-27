import pandas as pd
import altair as alt
from wcwidth import width

alt.renderers.enable('browser')
auction_data=pd.read_csv("Datasets/auction.csv")

auction_data=auction_data.sample(2500)   # select 2500 samples randomly

auction_xbox=auction_data[auction_data["item"]=="Xbox game console"]  #filter data

chart1=alt.Chart(auction_xbox,height=400,width=600).mark_boxplot(size=100).encode(x="item",y="bid",color="auction_type")
chart1.show()

chart2=alt.Chart(auction_data,height=400,width=600).mark_boxplot(size=100).encode(x="item",y="bid")
chart2.show()

chart3=alt.Chart(auction_xbox).transform_density("price",as_=["price","density"]).mark_area().encode(y="density:Q",x="price").properties(width=300)
chart3.show()

#violin chart
chart4=alt.Chart(auction_xbox).transform_density("price",as_=["price","density"]).mark_area().encode(y=alt.Y("density:Q",stack="center"),x="price").properties(width=300)
chart4.show()

chart5=alt.Chart(auction_data).transform_density("price",as_=["price","density"],extent=[0,4500],groupby=["item"]).mark_area(orient="horizontal").encode(x=alt.X("density:Q",stack="center"),y="price",column="item",color="item").properties(width=300)
chart5.show()