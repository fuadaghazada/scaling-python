import time

from rq import Queue
from redis import Redis
import requests

q = Queue(name="sum", connection=Redis())

job = q.enqueue(sum, [43, 77],
                ttl=60, result_ttl=300)
# While the URL is fetched, it's possible to do anything else.
# Wait until the result is ready.
while job.result is None:
    time.sleep(1)

print(job.result)