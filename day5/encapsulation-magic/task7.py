import time 
class Timer:
    def _enter_(self):
        self.start = time.time()
        
    def _exit_(self, *args):
     end = time.time()
     print("Time:", end - self.start, "seconds")
     with Timer():
        for i in range(1000000):
            pass