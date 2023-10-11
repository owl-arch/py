##
# Tasks e Subtasks
# https://gist.github.com/lrvick/1040562/b3b8b0033074f66621d81d7ef153a13cdd46a721

import celeryconfig

from celery.result import AsyncResult 

from celery.execute import send_task

import time

def get_results(queries):
    result = send_task('task1',queries)
    results = result.get()
    #this does not return ids until _after_ all the tasks are complete, for some reason.
    while results:
        #pop first off queue, this will shorten the list and eventually break out of while
        first_id = results.pop(0) 
        r = AsyncResult(first_id)
        if not r.ready():
            results.append(first_id) #add it back to the bottom o fthe queue
        else:
            out = r.get()
            if out: print out

get_results(['a','b','c'])