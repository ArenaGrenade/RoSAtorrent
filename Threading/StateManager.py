from .TaskQueue import TaskQueue

# TODO: Maybe we should push these task queue stuff to TaskQueue.py and abstract it - needs init, getting, joining, informing that a task has completed
class StateManager:
    def __init__():
        self.task_queue = TaskQueue()
        
    def get_task():
        return self.task_queue.get()

    def cleanup():
        self.task_queue.join()
