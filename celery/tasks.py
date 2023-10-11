##
# Tasks e Subtasks
# https://gist.github.com/lrvick/1040562/b3b8b0033074f66621d81d7ef153a13cdd46a721

from celery.decorators import task

@task
def task1(queries):
    task_ids = []
    for query in queries:
        result = task2.delay(query)
        task_ids.extend(result.get())
    return task_ids

@task
def task2(query):
   task_ids = []
   i = 0
   while i < 20:
      i += 1
      result = task3.delay()
      task_ids.append(result.task_id)
   return task_ids

@task
def task3()
    time.sleep(2)
    return 'done' 