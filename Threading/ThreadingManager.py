from .StateManager import StateManager
from .ThreadHandler import ThreadHandler

class ThreadingManager:
    def __init__():
        self.state = StateManager()
        self.active_threads = []
        
    def run(max_threads=4):
        while True:
            if len(self.active_threads) < max_threads:
                thread_properties = self.state.get_task()
                thread_handler = ThreadHandler(thread_properties=thread_properties)
                self.active_threads.append(thread_handler)
            
            completed_threads = []
            for tidx, thread_handler in enumerate(self.active_threads):
                if not thread_handler.is_alive():
                    completed_threads.append(tidx)
            self.active_threads = [th for ti, th in enumerate(self.active_threads) if ti not in completed_threads]
            
        self.state.cleanup()
