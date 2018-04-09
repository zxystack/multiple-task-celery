# *-* coding: utf-8 *-*

import time
from celery import Celery

celeryapp = Celery(broker='redis://localhost:6379/2')
celeryapp.config_from_object('celeryconfig')

@celeryapp.task
def video():
    print "processing video"
    time.sleep(10)

@celeryapp.task
def image():
    print "processing image"
    time.sleep(5)

@celeryapp.task
def common():
    print "processing common"
    time.sleep(3)
