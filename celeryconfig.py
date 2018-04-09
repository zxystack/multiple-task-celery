# *-* coding:utf-8 *-*

from kombu import Exchange, Queue

CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_BROKER = 'redis://locahost:6379/1'

default_exchange = Exchange('default', type='direct')
media_exchange = Exchange('media', type='direct')

CELERY_QUEUES = (
    Queue('default', default_exchange, routing_key='default'),
    Queue('videos', media_exchange, routing_key='media.video'),
    Queue('images', media_exchange, routing_key='media.image'),
)

CELERY_DEFAULT_QUEUE = 'default'
CELERY_DEFAULT_EXCHANGE = 'default'
CELERY_DEFAULT_ROUTTING_KEY = 'default'

CELERY_ROUTES ={
        'tasks.image': {

            'queue': 'images',
            'routing_key': 'media.image'
            },

        'tasks.video': {

            'queue': 'videos',
            'routing_key': 'media.video'
            }
}
CELERY_IMPORTS = ('tasks')

