from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crm_back.settings') # set django settimg module
app = Celery('crm_back') # create celery object with project name


app.config_from_object('django.conf:settings', namespace='CELERY') # discover all variables at setting which statrt at CELERY
app.autodiscover_tasks() # found aall celery tasks in our project


# crontab(minute="*/1") execute every minute
# minute='0', hour='12'
app.conf.beat_schedule = {
    'check-student-field-every-12am':{
        'task': 'student.tasks.get_checked_groups',
        'schedule': crontab(minute="*/1"), # execute every day at 12 midday
    }
}