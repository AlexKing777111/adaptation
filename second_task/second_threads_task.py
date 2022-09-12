import threading
import time
from random import randint


class IntervalThread(threading.Thread):
    def __init__(
        self,
        name=None,
        group=None,
        target=None,
        args=(),
        kwargs=None,
        *,
        daemon=None,
        interval=2,
    ):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.interval = interval

    def run(self):
        print(f"---Поток {threading.currentThread().name} начал работу.---")
        time.sleep(randint(1, 10))
        print(f"---Поток {threading.currentThread().name} закончил работу.---")


def thr1_starter(interval, name):
    thr1 = IntervalThread(interval=interval, name=name)
    time.sleep(interval)
    thr1.start()
    return thr1


def thr2_starter(interval, name):
    thr2 = IntervalThread(interval=interval, name=name)
    time.sleep(interval)
    thr2.start()
    return thr2


if __name__ == "__main__":
    thr1 = thr1_starter(interval=0, name="Gena")
    thr2 = thr2_starter(interval=0, name="artur")
    while True:
        if not thr1.is_alive():
            thr1 = thr1_starter(interval=10, name="Gena")
        elif not thr2.is_alive():
            thr2 = thr2_starter(interval=1, name="artur")
