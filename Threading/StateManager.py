from queue import PriorityQueue

# TODO: Maybe we should push these task queue stuff to TaskQueue.py and abstract it - needs init, getting, joining, informing that a task has completed
class StateManager:
    def __init__(self):
        self._task_queue = PriorityQueue()
        
    @property
    def task(self):
        return self._task_queue.get()
    
    @task.setter
    def task(self, priority_proc_pair):
        self._task_queue.put(priority_proc_pair)
    
    @task.deleter
    def task(self):
        self._task_queue.task_done()
