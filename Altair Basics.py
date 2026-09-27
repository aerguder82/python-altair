import pandas as pd
import altair as alt
from wcwidth import width

data = pd.DataFrame({'Categories': ['Clothing',
                                    'Electronics',
                                    'Furniture',
                                    'Health',
                                    'Kitchen'],
                     'Sales': [110, 343, 201, 120, 278]})

chart1=alt.Chart(data,height=200,width=300).mark_bar().encode(x="Categories",y="Sales")
chart2=alt.Chart(data).mark_bar().encode(x="Categories:O",y="Sales:Q").properties(height=600,width=800,title="Sales by product numbers")
alt.renderers.enable('browser')
#chart1.show()
#chart2.show()


wide_form = pd.DataFrame({'Year': [2018, 2019, 2020],
                          'Clothing': [110, 101, 129],
                          'Furniture':[201, 184, 195],
                          'Health': [120, 132, 133]
                         })

long_form = pd.DataFrame({'Year': [2018, 2019, 2020,
                                   2018, 2019, 2020,
                                   2018, 2019, 2020],
                          'Category': ['Clothing', 'Clothing', 'Clothing',
                                       'Furniture', 'Furniture', 'Furniture',
                                       'Health', 'Health', 'Health'],
                          'Sales': [110, 101, 129,
                                    201, 184, 195,
                                    120, 132, 133]
                         })

chart3=alt.Chart(long_form).mark_line().encode(x="Year:O",
                                                y="Sales:Q",
                                              color="Category:N"
                                                ).properties(height=400,
                                                    width=600,
                                                     title="Annual Sales by Category")
chart3.show()


transformed=wide_form.melt("Year",var_name="Category",value_name="Sales")


chart4=alt.Chart(transformed).mark_line().encode(x="Year:O",
                                                y="Sales:Q",
                                              color="Category:N"
                                                ).properties(height=400,
                                                    width=600,
                                                     title="Annual Sales by Category")

chart4.show()