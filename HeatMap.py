import altair as alt
import pandas as pd

alt.renderers.enable('browser')
cars_data=pd.read_csv("Datasets/car_price_data.csv")

base = alt.Chart(cars_data, height = 300, width = 600).transform_aggregate(
        num_items = 'count():Q',
        avg_price = 'mean(price):Q',
        avg_hp = 'mean(horsepower):Q',
        avg_citympg = 'mean(citympg):Q',
        groupby=['carbody', "drivewheel"]
       ).encode(
        x = alt.X('carbody'),
        y = alt.Y('drivewheel')
       )
heatmap = base.mark_rect().encode(
    color=alt.Color('num_items:Q'),
    tooltip = ['avg_price:Q','num_items:Q']
    )

heatmap.show()