import celery

app = celery.Celery('celery-test',
                    broker='redis://localhost',
                    backend='redis://localhost')

@app.task
def getWordCount(text):
    res = {}
    for word in text.split():
        _word = word.lower()
        if not res.get(_word):
            res[_word] = 1
        else:
            res[_word] += 1
    
    return res

if __name__ == '__main__':
    texts = ["Pickle in Python is primarily used in serializing and deserializing a Python object structure. In other words, it's the process of converting a Python object into a byte stream to store it in a file/database, maintain program state across sessions, or transport data over the network.", 
             "In some countries (e.g., the United States and Canada), essays have become a major part of formal education.",
             "Essays belong to a literary species whose extreme variability can be studied most effectively within a three-poled frame of reference"]

    results = []
    ##### Write code here ######
    for text in texts:
        result = getWordCount.delay(text)
        results.append(result)

    ##### Code until here ######
    for result in results:
        print("Task state: %s" % result.state)
        print("Result: %s" % result.get())
        print("Task state: %s" % result.state)
