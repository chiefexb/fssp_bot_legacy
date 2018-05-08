import requests
import json
viber_url = "https://chatapi.viber.com/pa"
viber_agent = "ViberBot-RoboInterativo"
def set_webhook (tok,hook_url):
    p={"auth_token":tok ,
       "url":hook_url,
       "is_inline":False}
    p["event_types"]=["delivered","seen","failed","subscribed", "unsubscribed",  "conversation_started" ]
    p=json.dumps(p)
    print (p)

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': viber_agent})
    r = requests.post(viber_url + '/set_webhook', data=p, headers=headers)
    return json.loads(r.text)
def send_message (tok,text):
    k={
	"Type": "keyboard",
	"Buttons": [{
		"Columns": 3,
		"Rows": 2,
		"Text": "Smoking",
		"TextSize": "medium",
		"TextHAlign": "center",
		"TextVAlign": "bottom",
		"ActionType": "reply",
		"ActionBody": "Smoking",
		"BgColor": "#f7bb3f",
		"Image": ""
	}]
}
	
    p={
   "receiver":"qhqxCNETGiLJmLZb+prEDQ==",
   "min_api_version":1,
   "sender":{
      "name":"Робо пристав",
      "avatar":"https://fssp.robointerativo.ru/static/ava.jpg"
   },
   "tracking_data":"tracking data",
   "type":"text",
   "text":"Hello world!"
}
    p["keyboard"]=k
    p["auth_token"]=tok

    p=json.dumps(p)
    print (p)

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': viber_agent})
    r = requests.post(viber_url + '/send_message', data=p, headers=headers)
    return json.loads(r.text)
