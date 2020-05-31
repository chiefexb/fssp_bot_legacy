import  requests

webhook='https://bot.robointerativo.ru/webhook'
#6bJ8v8%ElDb@'
token="511422853:AAFV6Gb2FswiEc8MNVbeirJkR_5LN3cUCfI"
api_method="setWebhook"

#deleteWebhook
#"getWebhookInfo"
#getMe
#url= 'https://api.telegram.org/bot{}/{}'.format (token,api_method)
url=webhook
print (url)
payload={}
#payload['url']=webhook
#r=requests.get (url)
r=requests.post (url,payload)
print (r.text)
