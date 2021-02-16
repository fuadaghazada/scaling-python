import celery
import requests
import tenacity

app = celery.Celery('celery-proj',
                    broker='redis://localhost',
                    backend='redis://localhost')

@app.task()
@tenacity.retry(
    wait=tenacity.wait_fixed(5),
    stop=tenacity.stop_after_attempt(5)
)
def getURL(url_to_crawl):
    response = requests.get(url_to_crawl)
    if response.status_code != 200:
        raise RuntimeError
    return response.text

if __name__ == '__main__':
    ## This urls list contains some url to be fetched
    urls = ["http://educative.io", "http://example.org/", "http://example.com"]

    results = []

    # Add tasks to queue here
    for url in urls:
        task = results.append(
            getURL.delay(url)
        )
        
    # Print the tasks states here
    for task in results:
        print("Task state:", task.state)
        print("Task result:", task.get())
        print("Task state:", task.state)