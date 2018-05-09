import requests
import json
viber_url = "https://chatapi.viber.com/pa"
viber_agent = "ViberBot-RoboInterativo"

class keyboard_button(object):
    def __init__(self, *args,**kwargs):
         self.Columns    = kwargs.get('Columns', 6)
         self.Rows       = kwargs.get ('Rows',1)
         self.ActionBody = kwargs.get ('ActionBody','reply')
         self.ActionType = kwargs.get ('ActionType', 'reply')
         self.BgColor    = kwargs.get ('BgColor','#ffd800')
         self.Text       = kwargs.get ('Text', 'text')
         self.TextHAlign = kwargs.get ('TextHAlign',"center")
         self.TextVAlign = kwargs.get ('TextVAlign', "bottom")
    def todict(self):
        return dict(self.__dict__)
class keyboard (object):
   def __init__(self):
       self.Type='keyboard'
       self.Buttons=[]
   def add_button(self,*args,**kwargs):
       self.Buttons.append (keyboard_button(*args,**kwargs))

   
   def todict(self):
       d=dict(self.__dict__)
       b=[]
       for bb in self.Buttons:
           b.append (bb.todict() )
       d.update({'Buttons':b})
       return d
def set_webhook (tok,hook_url):
    p={"auth_token":tok ,
       "url":hook_url,
       "is_inline":False}
    p["event_types"]=["delivered","seen","failed","subscribed", "unsubscribed",  "conversation_started" ]
    p=json.dumps(p)
    log.info('API '+ str(p) )

    headers = requests.utils.default_headers()
    headers.update({'User-Agent': viber_agent})
    r = requests.post(viber_url + '/set_webhook', data=p, headers=headers)
    return json.loads(r.text)
def send_message (log,tok,text,receiver,sender,keyboard):
    p={}
    p['receiver']=receiver
    p['min_api_version']=1    
    p['sender']={'name':sender,'avatar':''} 
    p['tracking_data']='tracking data'
    p['type']='text'   
    p['text']=text
    p["auth_token"]=tok
    if keyboard != None:
        p['keyboard']=keyboard.todict()
    p=json.dumps(p)
    log.info('WEBHOOK '+ p )
    headers = requests.utils.default_headers()
    headers.update({'User-Agent': viber_agent})
    r = requests.post(viber_url + '/send_message', data=p, headers=headers)
    return json.loads(r.text)

class user (object):
    def __init__(self,js):
         self.avatar=js['avatar']
         self.country=js['country']
         self.id= js['id']
         self.language= js['language'] 
         self.name= js['name']   
         self.api_version=js['api_version']
    
class message(object):
    def __init__(self,js):
        self.text=js['text']
        self.type=js['type'] 
class message_request(object):
     def __init__(self,js):
         js=json.loads(js)
         self.event=js['event']
         if js['event']=='message':
            self.sender=user(js['sender'])
            self.message=message(js['message'])
            self.message_token=js['message_token']
            self.silent= js['silent']
            self.timestamp= js['timestamp']

