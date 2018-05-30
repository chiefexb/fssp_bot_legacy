#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import time

def format_ip(msg):

    fmsg=[]
    fmsg.append('<b>Должник (физ. лицо: ФИО, дата и место рождения; </b>')
    fmsg.append (msg['name'])
    fmsg.append ('<b>ИСПОЛНИТЕЛЬНОЕ ПРОИЗВОДСТВО:</b>')
    fmsg.append(msg['exe_production'])
    fmsg.append ('<b>ИСПОЛНИТЕЛЬНЫЙ ДОКУМЕНТ:</b>')
    fmsg.append(msg['details'])
    if len (msg['ip_end'])>0:
        fmsg.append ('<b>Дата окончания, статья</b>')
        fmsg.append(msg['ip_end']) 
    if len (msg['subject'])>0:
        fmsg.append ('<b>Предмет исполнения:</b>')
        fmsg.append(msg['subject'])
        
    fmsg.append ('<b>Отдел судебных приставов </b>')
    fmsg.append(msg['department'])
    fmsg.append ('<b>Судебный пристав исполнитель</b>')
    fmsg.append(msg['bailiff'].replace('<br>',' '))
   
    return fmsg


class FsspApi(object):
    base_url="https://api-ip.fssprus.ru/api/v1.0"
    region = ''
    lastname = ''
    firstname = ''
    r_status_code=''
    status = -1
    answ = ''
    result = ''
    task = ''
    token = ''

    def __init__(self,token):
        self.token=token
    
    def set_lastname(self,lastname):
        self.lastname=lastname

    def set_firstname(self,firstname):
        self.firstname=firstname
        
    def set_region(self,region):
        self.region=region
     
    def search_phisycal(self):
        print({'token': self.token,
                  'region': self.region,
                  'firstname': self.firstname,
                  'lastname': self.lastname})
         
        req=requests.get(self.base_url+'/search/physical', params=
        {'token': self.token,
         'region': self.region,
         'firstname': self.firstname,
         'lastname': self.lastname
         })
        print (req.url)
        if (req.status_code==200):
            # print (req.__dir__,req.url)
            # print ((req.content), type (req.content))
            jsdata = json.loads (req.text)
            self.task=jsdata['response']['task']
        self.r_status = req.status_code
        
    def get_status_task(self):
        rr = False
        req=requests.get(self.base_url+'/status', params=
        {
            'token': self.token,
            'task': self.task
        })
        print (self.task,req)
        print (req.url)
        if req.status_code==200:
            print (req.text)
            jsdata = json.loads (req.text)
            self.status = jsdata['response']['status']
            print (type(jsdata['response']['status']),
                   jsdata['response']['status'])
            if jsdata['response']['status'] == 0:
                rr = True
            elif jsdata['response']['status'] == 3:
                rr = True
        self.r_status = req.status_code

        return rr

    def wait_for(self):
        
        while 1:
            print(self.status)
            time.sleep (5)
            if self.get_status_task():
                break

    def get_result(self):
        req=requests.get(self.base_url+'/result', params=
        {
            'token': self.token,
            'task': self.task
        })
        print(req.url)

        if req.status_code == 200:
            jsdata = json.loads(req.text)
            list_ip = jsdata['response']['result'][0]['result']
            self.result = list_ip
    def get_res(self):
        pass
      
