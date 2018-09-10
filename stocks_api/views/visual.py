from ..models.schemas import StocksInfoSchema
from pyramid_restful.viewsets import APIViewSet
from sqlalchemy.exc import IntegrityError, DataError
from pyramid.view import view_config
from pyramid.response import Response
from ..models import StocksInfo
import requests
import json
import pandas as pd
import numpy as np
import datetime as dt
import requests
import json
# import matplotlib
# import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as poly
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from bokeh.charts import Bar
import bokeh.plotting as bk
from bokeh.models import HoverTool, Label, BoxZoomTool, PanTool

# %matplotlib inline

# matplotlib.rcParams['figure.figsize'] = [120.0, 80.0]
API_URL = 'https://api.iextrading.com/1.0'


@view_config(route_name='visual', renderer='json', request_method='POST')
def lookup(request):
    symbol = request.matchdict['symbol']
    print(symbol)
    r_company_info = requests.get(f'{API_URL}/stock/{symbol}/company')
    json_company_info = r_company_info.json()
    company_name = json_company_info['companyName']
    company_name = company_name.split(' ')
    company_name = '_'.join(company_name)
    company_name = company_name.strip('.')


    try:
        kwargs = json.loads(request.body)
    except json.JSONDecodeError as e:
        return Response(json=e.msg, status=400)

    r = requests.get(f'{API_URL}/stock/{symbol}/chart/5y')
    json_data = r.json()

    pandas_df = pd.DataFrame(json_data)

    pandas_df.shape

    pandas_df.date = pd.to_datetime(pandas_df.date)

    seqs = np.arange(pandas_df.shape[0])
    pandas_df['seqs'] = pd.Series(seqs)

    pandas_df['changePercent'] = pandas_df['changePercent'].apply(lambda x: float(x))

    pandas_df['mid'] = pandas_df.apply(lambda x: ((x['open'] + x['close']) / 2), axis=1)

    pandas_df['height'] = pandas_df.apply(
        lambda x: x['close'] - x['open'] if x['close'] != x['open'] else 0.001
        , axis=1)
    hover = HoverTool(
            tooltips=[
                ('date', '@date'),
                ('low', '@low'),
                ('high', '@high'),
                ('open', '@open'),
                ('close', '@close'),
                ('percent', '@changePercent'),
            ]
    )

    TOOLS = [hover, BoxZoomTool(), PanTool()]

    if kwargs['chart'] == 'candlestick':
        inc = pandas_df.close > pandas_df.open
        dec = pandas_df.close < pandas_df.open
        w = .3

        sourceInc = bk.ColumnDataSource(pandas_df.loc[inc])
        sourceDec = bk.ColumnDataSource(pandas_df.loc[dec])
        p = bk.figure(plot_width=1500, plot_height=800, tools=TOOLS, title=f'{company_name}', toolbar_location='below')

        p.xaxis.major_label_orientation = np.pi/4
        p.grid.grid_line_alpha=w

        p.xaxis[0].axis_label = 'Date'
        p.yaxis[0].axis_label = 'Stock Price ($)'

        p.segment(pandas_df.seqs[inc], pandas_df.high[inc], pandas_df.seqs[inc], pandas_df.low[inc], color='green')

        p.segment(pandas_df.seqs[dec], pandas_df.high[dec], pandas_df.seqs[dec], pandas_df.low[dec], color='red')

        p.rect(x='seqs', y='mid', width=w, height='height', fill_color='green', line_color='green', source=sourceInc)

        p.rect(x='seqs', y='mid', width=w, height='height', fill_color='red', line_color='red', source=sourceDec)

        bk.save(p, f'./stocks_api/static/{company_name}_candle_stick.html', title=f'{company_name}_5y_candlestick')

    ## Graph gain vs. loss days
    if kwargs['chart'] == 'percent':

        pandas_df['pos_days'] = pandas_df.apply(lambda x: x['changePercent'] if x['changePercent'] >= 0 else 0, axis=1)

        pandas_df['neg_days'] = pandas_df.apply(lambda x: x['changePercent'] if x['changePercent'] < 0 else 0, axis =1)

        end_data = []
        end_data.insert(0, {'change': 0.00000, 'pos_days': 0.000, 'neg_days':0.000, 'seqs': 1259.0})
        pandas_df = pandas_df.append(end_data, ignore_index=False)
        start_data = []
        start_data.insert(0, {'change': 0.00000, 'pos_days': 0.000, 'neg_days':0.000, 'seqs': -1.0})
        pandas_df = pandas_df.append(start_data, ignore_index=False)

        percInc = bk.ColumnDataSource(pandas_df)
        percDec = bk.ColumnDataSource(pandas_df)

        bar_graph = bk.figure(plot_width=1500, plot_height=800, tools=TOOLS, title=f'{company_name}', toolbar_location='below')

        bar_graph.patch(x='seqs', y='neg_days', color='red', source=percDec)
        bar_graph.patch(x='seqs', y='pos_days', color='green', source=percInc)

        bk.save(bar_graph, f'./stocks_api/static/{company_name}_daily_percent_change.html', title=f'{company_name}_5y_percent_change')

    return Response(json='this works!', status=200)
