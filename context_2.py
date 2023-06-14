import time
from types import TracebackType

class RunningCodeJudge:
    def __init__(self):
        self.start = None

    
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.time() - self.start
        print(f'Время работы кода: {t} сек.')

        if exc_type is TypeError:
            return True

    def __str__(self):
        return 'Я таймер'
    

with RunningCodeJudge():
    my_list = [x for x in range(1, 1000000)]
    my_list -= 's'

