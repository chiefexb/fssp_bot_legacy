#!/usr/bin/python3
#coding: utf8
import time
from datetime import datetime
from mysqlapi import *


def start_job(**kwargs):
    p = MyData('/home/f.cnf', 'fsspbotdb')
    job = p.get_table('job')
    dt=datetime.now()
    job.add(start_date=dt, job_name='search_ip', status=1)
    job.save()


def main():
    # start search api
    start_job()


if __name__ == "__main__":

    main()