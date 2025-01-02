import time

class Timer:

    def __enter__(self):
        self.start = time.perf_counter()
        return self
    
    def __exit__(self, exc_type, exc_value, trace):
        self.stop = time.perf_counter()
        self.result = self.stop - self.start
        print(f"time spending : {self.result:.8}")
        return self.result
    


with Timer():
    n = 0
    for i in range(1000000):
        n += i