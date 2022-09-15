import threading
import time
from datetime import datetime
from random import randint


class IntervalThread(threading.Timer):
    def __init__(self, interval, function, name=None, args=[], kwargs=None):
        super().__init__(interval, function, args, kwargs)
        self.name = name


def work_imitation():
    event.clear()
    print(
        f"---Поток {threading.currentThread().name} "
        f"начал работу в {datetime.now().strftime('%H:%M:%S')}---"
    )
    time.sleep(randint(1, 10))
    print(
        f"---Поток {threading.currentThread().name} "
        f"закончил работу в {datetime.now().strftime('%H:%M:%S')}---"
    )
    event.set()


if __name__ == "__main__":
    event = threading.Event()
    thr1 = threading.Thread(target=work_imitation, name="first")
    thr1.start()
    thr2 = threading.Thread(target=work_imitation, name="second")
    thr2.start()
    thr3 = threading.Thread(target=work_imitation, name="third")
    thr3.start()
    thr4 = threading.Thread(target=work_imitation, name="fourth")
    thr4.start()
    thr5 = threading.Thread(target=work_imitation, name="fifth")
    thr5.start()
    while True:
        event.wait()
        if not thr1.is_alive():
            thr1 = IntervalThread(1, work_imitation, name="first")
            print(event.is_set())
            thr1.start()
            print(event.is_set())
        elif not thr2.is_alive():
            thr2 = IntervalThread(3, work_imitation, name="second")
            thr2.start()
        elif not thr3.is_alive():
            thr3 = IntervalThread(5, work_imitation, name="third")
            thr3.start()
        elif not thr4.is_alive():
            thr4 = IntervalThread(7, work_imitation, name="fourth")
            thr4.start()
        elif not thr5.is_alive():
            thr5 = IntervalThread(10, work_imitation, name="fifth")
            thr5.start()
