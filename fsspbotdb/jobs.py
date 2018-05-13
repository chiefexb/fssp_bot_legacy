#!/usr/bin/python3
#coding: utf8
import time
import configparser
from mysql import connector

def search_physical():
    sleep(60)
    print ("JW")
    return 1
class Job_State_Machine(object):
    def get_state():
        pass
    def __init__(self):
        pass
def get_active():
    for jj in act_jobs:
        if job_name=="search_physical":
            f= search_physical()
            if f>0:
               stop_job(jj)
def main ():
    config=configparser.ConfigParser()
    config.read('/home/f.cnf')
    client=config['client']
    conn=connector.connect(host                  = 'localhost',
                           database              = client['database'],
                           user                  = client['user'], 
                           password              = client['password'])
                   #        default-character-set = client['default-character-set'])
    cursor = conn.cursor()
    cursor.execute ('SELECT * FROM fsspbotdb_job where status=1')
    row=cursor.fetchone()
    conn.close()
    print (row)
    while 1:
        #get_job()
        pass
#p=Setting.objects.filter(valuename="VIBERTOKEN")
#             tok=p.values()[0]['value']
if __name__ == "__main__":
    main()
