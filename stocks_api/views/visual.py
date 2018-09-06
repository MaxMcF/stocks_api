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
import bokeh.plotting as bk
from bokeh.models import HoverTool, Label, BoxZoomTool, PanTool

# %matplotlib inline

# matplotlib.rcParams['figure.figsize'] = [120.0, 80.0]
API_URL = 'https://api.iextrading.com/1.0'
SYMBOL = 'v'


class VisualAPIView(APIViewSet):
    """This is going to listen to a request from a specific endpoint.
    """
    def list(self, id=None):
        r_company_info = requests.get(f'{API_URL}/stock/{SYMBOL}/company')
        json_company_info = r_company_info.json()
        company_name = json_company_info['companyName']

        r = requests.get(f'{API_URL}/stock/{SYMBOL}/chart/5y')


        json_data = r.json()

        pandas_df = pd.DataFrame(json_data)

        pandas_df.shape

        pandas_df.date = pd.to_datetime(pandas_df.date)

        seqs = np.arange(pandas_df.shape[0])
        pandas_df['seqs'] = pd.Series(seqs)

        pandas_df['changePercent'] = pandas_df['changePercent'].apply(lambda x: float(x))

        pandas_df.sample(10)

        pandas_df['mid'] = pandas_df.apply(lambda x: ((x['open'] + x['close']) / 2), axis=1)

        pandas_df['height'] = pandas_df.apply(
            lambda x: x['close'] - x['open'] if x['close'] != x['open'] else 0.001
            , axis=1)

        inc = pandas_df.close > pandas_df.open
        dec = pandas_df.close < pandas_df.open
        w = .3

        sourceInc = bk.ColumnDataSource(pandas_df.loc[inc])
        sourceDec = bk.ColumnDataSource(pandas_df.loc[dec])



        # seqs_change = np.arange(changePer.shape[0])
        # changePer['seqs_change'] = pd.Series(seqs)

        pos_days = pandas_df[pandas_df.changePercent >= 0]
        neg_days = pandas_df[pandas_df.changePercent < 0]

        percInc = bk.ColumnDataSource(pos_days)
        percDec = bk.ColumnDataSource(neg_days)

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

        p = bk.figure(plot_width=1500, plot_height=800, tools=TOOLS, title=f'{company_name}', toolbar_location='below')

        p.xaxis.major_label_orientation = np.pi/4
        p.grid.grid_line_alpha=w

        # descriptor = Label(x_offset=70, y_offset=70, text='')
        # p.add_layout(descriptor)

        p.xaxis[0].axis_label = 'Date'
        p.yaxis[0].axis_label = 'Stock Price ($)'



        p.segment(pandas_df.seqs[inc], pandas_df.high[inc], pandas_df.seqs[inc], pandas_df.low[inc], color='green')

        p.segment(pandas_df.seqs[dec], pandas_df.high[dec], pandas_df.seqs[dec], pandas_df.low[dec], color='red')

        p.rect(x='seqs', y='mid', width=w, height='height', fill_color='green', line_color='green', source=sourceInc)

        p.rect(x='seqs', y='mid', width=w, height='height', fill_color='red', line_color='red', source=sourceDec)

        company_name = company_name.split(' ')
        company_name = '_'.join(company_name)
        company_name = company_name.strip('.')

        bk.save(p, f'../static/{company_name}_candle_stick.html', title=f'{company_name}_5y_candlestick')

        ## Graph gain vs. loss days


        bar_graph = bk.figure(plot_width=1500, plot_height=800, tools=TOOLS, title=f'{company_name}', toolbar_location='below')

        bar_graph.patch(x='seqs', y='changePercent', color='red', source=percDec)
        bar_graph.patch(x='seqs', y='changePercent', color='green', source=percInc)


        bk.show(bar_graph)


        return Response(json='this works!', status=200)
