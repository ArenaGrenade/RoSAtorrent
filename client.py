from Threading.ThreadingManager import ThreadingManager
from CLI.runner import CLI_Thread

if __name__ == '__main__':
    threadManager = ThreadingManager()
    CLI_thread = CLI_Thread()
    
    # Add CLI Process to threading manager
    # threadManager.state.task = (1, CLI_thread)
    
    threadManager.run()
    # CLI_thread.run()
    
    print("Thread Manager Started.")
    threadManager.join()
