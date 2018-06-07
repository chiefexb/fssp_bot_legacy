#!/usr/bin/python3
#coding: utf8

import configparser

from time import *
from mysqlapi import *


def search_physical():
    sleep(6)
    print("JW")
    return 1


class JobStateMachine(object):
    def get_state():
        pass

    def __init__(self):
        self.job_name = ''

    def get_active(self):
        for jj in act_jobs:
            if self.job_name == "search_physical":
                f = search_physical()
                if f > 0:
                   stop_job(jj)

def main ():
    p = MyData('/home/f.cnf', 'fsspbotdb')
    job = p.get_table('job')
    # while 1:
    print(job.values())

#p=Setting.objects.filter(valuename="VIBERTOKEN")
#             tok=p.values()[0]['value']


if __name__ == "__main__":
    main()
