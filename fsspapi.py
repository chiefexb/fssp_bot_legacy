#!/usr/bin/python3
# -*- coding: utf-8 -*-
import requests

class FsspApi(object):
    base_url="https://api-ip.fssprus.ru/api/v1.0"
    par={}   
    def __init__(self,token):
        self.token=self.par['token']=token
    
    def set_param(self,par):
        for key in par.keys():
           self.par[key]=par[key]

    def set_lastname(self,lastname):
        self.par['lastname']=lastname

    def set_firstname(self,firstname):
        self.par['fistname']=firstname

    def set_region(self,region):
        self.par['region']=region

    def search_phisycal():
        req=requests.get(a.base_url+'/search/physical',params=self.par)
        if req.status==200:
           self.task=req.content['task']
        self.r_status=req.status
        
    def get_status_task(self):
        req=requests.get(a.base_url+'/search/physical',params=par)
        if req.status==200:
           self.status=req.content
        self.r_status=req.status
    
def main():
   pass
if __name__ == "__main__":
    main()
