import pandas as pd

import plotly
import plotly.graph_objs as go

from flask import Flask, render_template

app = Flask("CovidScatter")

# loading dataset - https://github.com/pcm-dpc/COVID-19/blob/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv
df = pd.read_csv('dpc-covid19-ita-andamento-nazionale.csv')

# creates a scatterplot using plotly and saves it as an html div
def generate_scatter(df):
    plotly_fig = go.Figure(data=go.Scatter(x=df["data"], y=df["totale_positivi"], mode="markers"))
    div = plotly.offline.plot(plotly_fig, include_plotlyjs=False, output_type='div', config={'displayModeBar': False})
    return div

@app.route('/', methods=['GET'])
def home():    
    div = generate_scatter(df)
    return render_template("scatter.html", item_text = div)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)