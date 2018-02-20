#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests
import json
import time


class FsspApi(object):
    base_url="https://api-ip.fssprus.ru/api/v1.0"
    region=''
    lastname=''
    firstname=''
    r_status_code=''
    status=-1
    def __init__(self,token):
        self.token=token
    
    def set_lastname(self,lastname):
        self.lastname=lastname

    def set_firstname(self,firstname):
        self.firstname=firstname

    def set_region(self,region):
        self.region=region

    def search_phisycal(self):
        
        req=requests.get(self.base_url+'/search/physical',params=
        {'token'    :self.token,
         'region'   :self.region,
         'firstname':self.firstname,
         'lastname' :self.lastname})
        if (req.status_code==200):
            #print (req.__dir__,req.url)
            #print ((req.content), type (req.content))
            jsdata=json.loads (req.text)
            self.task=jsdata['response']['task']
        self.r_status=req.status_code
        
    def get_status_task(self):
        rr=False
        req=requests.get(self.base_url+'/status',params=
        {'token':self.token,
        'task':self.task})
        print (self.task,req)
        if req.status_code==200:
           print (req.text)
           jsdata=json.loads (req.text)
           self.status=jsdata['response']['status']
           print (type (jsdata['response']['status']),jsdata['response']['status'])
           if jsdata['response']['status']==0:
               rr=True
           elif jsdata['response']['status']==3:
               rr=True
        self.r_status=req.status_code
        return rr
    def wait_for(self):
        
        while  1:
             print (self.status)
             time.sleep (5)
             if self.get_status_task():
                 break
    def get_result(self):
        req=requests.get(self.base_url+'/result',params=
        {'token':self.token,
        'task':self.task})
        if (req.status_code==200):
            print (req.text)
def main():
   pass
if __name__ == "__main__":
    main()
