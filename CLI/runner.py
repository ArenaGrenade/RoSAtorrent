import threading
import time

class CLI_Thread(threading.Thread):    
    def run(self):
        print("""Welcome to RoSA-Torrent!""")
        time.sleep(10)
        return
