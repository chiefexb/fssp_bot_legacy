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

