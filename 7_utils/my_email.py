#
# my_app__init__.py
#

from __future__ import absolute_import

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

from .celery_settings import app as celery_app


#
#  my_app\email\tasks.py
#

from __future__ import absolute_import
from my_app.celery_settings import app

# here i only define the task skeleton because i'm executing this task on remote workers !
@app.task(name='email_task', bind=True, max_retries=3, default_retry_delay=1)
def email_task(self, job, email):
    try:
        print("x")
    except Exception as exc:
        self.retry(exc=exc)


#
# Worker\tasks.py
#

from __future__ import absolute_import
from celery.utils.log import get_task_logger
from celery import Celery


logger = get_task_logger(__name__)
app = Celery('CapValue', broker='amqp://soufiaane:C@pV@lue2016@cvc.ma/cvcHost', backend='redis://:C@pV@lue2016@cvc.ma:6379/0')

@app.task(name='email_task', bind=True, max_retries=3, default_retry_delay=1)
def email_task(self, job, email):
    try:
        """
        The actual implementation of the task
        """
    except Exception as exc:
        self.retry(exc=exc)        