##pip install pycoingecko
##pip install plotly --deprecated
##pip install chart-studio

from pycoingecko import CoinGeckoAPI
from chart_studio import plotly as go
import pandas as pd

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

bitcoin_price_data = bitcoin_data['prices']
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp','Price'])
data['Date'] = pd.to_datetime(data['TimeStamp'], unit='ms')
candlestick_data = data.groupby(data.Date.dt.date).agg({'Price': ['min','max','first','last']})

fig = go.Figure ()

