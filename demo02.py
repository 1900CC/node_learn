def say():
    print("Hello!")

import threading
timer = threading.Timer(3, say)
timer.start()