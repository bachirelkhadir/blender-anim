#!/usr/bin/env python3

import plotly.express as px
import pandas as pd

def outline_to_gantt(outline):
    outline = pd.DataFrame(outline)
    fig = px.timeline(outline, x_start="start", x_end="end", y="name",
                      color="animation")
    fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
    outline['delta'] = 10 # outline['end'] - outline['start']
    fig.layout.xaxis.type = 'linear'
    fig.data[0].x = outline.delta.tolist()
    #fig = fig.full_figure_for_development(warn=False)
    print(outline.tail())
    return fig
