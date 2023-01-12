# パーソナルアクセストークンでの認証
from pprint import pprint
import requests as r
from requests.auth import HTTPBasicAuth
import json
def req_w_personal_token():
    url = 'https://api.github.com/users/ao-tanaka'
    response = r.request('GET', url,
                         auth=HTTPBasicAuth('ao-tanaka',                          # ユーザ名
                                            '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')) # トークン
    #pprint(dict(response.headers))
    #pprint(response.json())
    json_obj = response.json()
    CONSUMER_KEY = json_obj['url']
    print(CONSUMER_KEY)
    return

req_w_personal_token()
