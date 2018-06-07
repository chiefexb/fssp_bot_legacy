#!/usr/bin/python3
#coding: utf8

import configparser

from time import *
from mysqlapi import *
from api.fsspapi import *

def search_physical():
    sleep(6)
    print("JW")
    return 1


def main():

    p = MyData('/home/f.cnf', 'fsspbotdb')
    setting = p.get_table('setting')
    setting.filter(valuename='FSSPTOKEN')
    val = setting.values()[0][1]
    print(val)
    job = p.get_table('job')
    # while 1:
    print(job.values())

#p=Setting.objects.filter(valuename="VIBERTOKEN")
#             tok=p.values()[0]['value']


if __name__ == "__main__":
    main()
