import requests, json, time, hmac, hashlib

class api():
  def __init__(self, **kwargs):
    self.base = 'https://coincheck.com'
    self.connection = requests.Session()
    self.access_token = kwargs.get('access_token', 'LRM_Pw0_ZNLRW3ie')
    self.access_key = kwargs.get('access_key', 'y89yuL_VNndfKIfnP_jM2qYjl41zsDwx')
  
  def nounce(self):
    return str(int(time.time() * 1000000000))
  
  def make_header(self, url,access_key=None,secret_key=None):
    nonce = self.nounce()
    url    = url
    message = nonce + url
    signature = hmac.new(secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()
    headers = {
       'ACCESS-KEY'      : access_key,
       'ACCESS-NONCE'    : nonce,
       'ACCESS-SIGNATURE': signature
    }
    return headers
    
  def public_request(self, **kwargs):
    endpoint = kwargs.get('endpoint')
    url = self.base + endpoint
    response = self.connection.get(url).json()
    return response
  
  def private_request(self, **kwargs):
    endpoint = kwargs.get('endpoint')
    url = self.base + endpoint
    headers = self.make_header(url, self.access_token, self.access_key)
    response = self.connection.get(url, headers=headers).json()
    return response
  
  def get_orderbook(self, **kwargs):
    endpoint = '/api/order_books'
    response = self.public_request(endpoint=endpoint)
    if kwargs.get('count'):
      response['bids'] = response['bids'][0:kwargs.get('count')]
      response['asks'] = response['asks'][0:kwargs.get('count')]
    return response
  
  def accounts_balance(self):
    endpoint = '/api/accounts/balance'
    response = self.private_request(endpoint=endpoint)
    return response
    
coincheckapi = api()