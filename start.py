import requests
import json

url = 'https://oapi.dingtalk.com/robot/send?access_token=dfb282779fa574887abaade18616db9be415fcc4b11289a6bd487a59f2b5a641'

requests.post(url,
    headers={'Content-Type': 'application/json'},
    data=json.dumps({"msgtype": "text",
        "text": {
             "content": "消息,我是python1235"
        }
      })
)