import altair as alt
import pandas as pd
from altair.utils.data import DataTransformerRegistry
from vega_datasets import data
from wcwidth import width

alt.renderers.enable('browser')

data.world_110m()

countries=alt.topo_feature(data.world_110m.url,"countries")
chart_geo=alt.Chart(countries,width=600).mark_geoshape(fill="skyblue",stroke="grey").project("equirectangular")
chart_geo.show()

chart_geo=alt.Chart(countries,width=600).mark_geoshape(fill="skyblue",stroke="grey").project("orthographic")
chart_geo.show()

chart_geo=alt.Chart(countries,width=600).mark_geoshape(fill="skyblue",stroke="grey").project("orthographic").configure_projection(center=[-50,15])
chart_geo.show()

world_offices=pd.DataFrame({"City":["Tokyo","Addis Ababa","Santiago"],
                            "Lattitude":[35.65,9.00,-33.45],
                            "Longitude":[20,53,67],
                            "NumofEmployees":[100,50,20]})
background=alt.Chart(countries,
                     width=600).mark_geoshape(fill="skyblue",
                                              stroke="grey",
                                              opacity=0.4).project("equirectangular")
points=alt.Chart(world_offices).mark_circle(size=60).encode(longitude="Longitude:Q",
                                                            latitude="Lattitude:Q",
                                                            color=alt.value("red"),
                                                            size="NumofEmployees:Q")
(background+points).show()


coffee_data=pd.read_csv("Datasets/coffee_data.csv")
coffee_data.dropna(inplace=True)

#drop some columns
coffee_data.drop(["Store Name",
                  "Postcode",
                  "Phone Number",
                  "Timezone"],
                 axis=1,
                 inplace=True)

US_data=coffee_data.loc[coffee_data["Country"]=="US"]

alt.data_transformers.disable_max_rows()
states=alt.topo_feature(data.us_10m.url,feature="states")
background=alt.Chart(states).mark_geoshape(fill="lightgray",
                                           stroke="whites").properties(width=600,
                                                                       height=400).project("albersUsa")
points=alt.Chart(US_data).mark_circle().encode(longitude="Longitude:Q",
                                               latitude="Latitude:Q",
                                               tooltip=["State/Province","City","Street Address"]).properties(title="Coffee Shops in the US")
(background+points).show()

points=alt.Chart(US_data).transform_aggregate(latitude="mean(Latitude):Q",
                                              longitude="mean(Longitude):Q",
                                              count="count()",
                                              groupby=["State/Province"]).mark_circle().encode(longitude="longitude:Q",
                                                                                               latitude="latitude:Q",
                                                                                               size=alt.Size("count:Q",title="Count of Coffee Shops"),
                                                                                               color=alt.value("steelblue"),
                                                                                               tooltip=["State/Province:N","count:Q"]).properties(title="Number of Coffee Shops in US")
(background+points).show()