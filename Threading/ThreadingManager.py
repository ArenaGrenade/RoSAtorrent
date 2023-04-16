import threading
from .StateManager import StateManager

class ThreadingManager(threading.Thread):
    def __init__(self, max_threads=4):
        super().__init__()
        self.state = StateManager()
        self.active_threads = []
        self.max_threads = max_threads
        
    def run(self):
        while True:
            print("Awaiting New Processes")
            if len(self.active_threads) < self.max_threads:
                priority, thread_handler = self.state.task
                thread_handler.run()
                self.active_threads.append(thread_handler)
                print("Got a Process")
            
            completed_threads = []
            for tidx, thread_handler in enumerate(self.active_threads):
                if not thread_handler.is_alive():
                    print("process complete")
                    completed_threads.append(tidx)
                    del self.state.task
            self.active_threads = [th for ti, th in enumerate(self.active_threads) if ti not in completed_threads]
            
        self.state.cleanup()
