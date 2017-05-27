import Settings
import json, base64, hashlib, urlparse, hmac, time, websocket, thread, copy
from websocket import create_connection
from coincheck import *

bids = []
asks = []

coincheckapi.get_orderbook()

raise SystemExit

def on_message(ws, message):
  global bids, asks
  message = json.loads(message)
  
  print(message[1]['bids'])
  

def on_error(ws, error):
  print(error)

def on_close(ws):
  print('Connection closed')

def on_open(ws):
  request = {"type": "subscribe", "channel": "btc_jpy-orderbook"}
  ws.send(json.dumps(request))
  print('Requested orderbook updates')

websocket.enableTrace(True)
ws = websocket.WebSocketApp(Settings.url,
  on_message = on_message,
  on_error = on_error,
  on_close = on_close
)
ws.on_open = on_open
ws.run_forever()