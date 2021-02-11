import threading
import cotyledon
import time

class PrintService(cotyledon.Service):
    name = "printer"

    def __init__(self, worker_id):
        super(PrintService, self).__init__(worker_id)
        self._shutdown = threading.Event()
    
    def run(self):
        while not self._shutdown.is_set():
            print("Doing stuff")
            time.sleep(1)
    
    def terminate(self):
        self._shutdown.set()


manager = cotyledon.ServiceManager()
manager.add(PrintService, 2)
manager.run()