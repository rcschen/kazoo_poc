from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab
from datetime import timedelta

app = Celery('gg',
             broker='amqp://',
             backend='amqp://')
#             include=['c_2_in_app.tasks'])
#             include=['c_2_in_app.tasks'])

# Optional configuration, see the application user guide.
app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'workers.tasks.add',
#        'schedule': crontab(minute='*'),
        'schedule': timedelta(seconds=1),
        'args': (16, 16),
    },
}
app.conf.update(
    result_expires=3600,
)
import sys
if __name__ == '__main__':
    print '>>>>' ,sys.argv
    app.start()
