#!/usr/bin/python3
#coding: utf8
import time
from fsspbotdb.models import *


def start_job():
    p=Job(start_date= datetime.datetime.now(), job_name='search_physical', status=1)
    p.save()


def stop_job(p):
    p=Job(end_date= datetime.datetime.now(), job_name='search_physical', status=10)
    p.save()
    #sys_def=p.values()[0]['value']

#def search_physical():
