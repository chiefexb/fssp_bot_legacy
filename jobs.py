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
    fssp_token = setting.values()[0][1]
    fssp = FsspApi(fssp_token)
    fssp.set_firstname('Сергей')
    fssp.set_lastname('Шило')
    fssp.set_region('09')
    tsk = fssp.search_phisycal()
    job = p.get_table('job')
    # while 1:
    print(tsk)

#p=Setting.objects.filter(valuename="VIBERTOKEN")
#             tok=p.values()[0]['value']


if __name__ == "__main__":
    main()
