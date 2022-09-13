import threading
import time
from datetime import datetime
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


def work_imitation():
    event.clear()
    print(
        f"---Поток {threading.currentThread().name} "
        f"начал работу в {datetime.now()}.---"
    )
    time.sleep(randint(1, 10))
    print(
        f"---Поток {threading.currentThread().name} "
        f"закончил работу в {datetime.now()}.---"
    )
    thr_reset(
        name=threading.currentThread().name,
        interval=threading.currentThread().interval,
        target=work_imitation,
    )
    event.set()


def thr_reset(interval, target, name=None):
    event.clear()
    time.sleep(interval)
    IntervalThread(name=name, interval=interval, target=target).start()


if __name__ == "__main__":
    event = threading.Event()
    event.set()
    IntervalThread(
        name="10 second", interval=10, target=work_imitation
    ).start()
    IntervalThread(name="7 second", interval=7, target=work_imitation).start()
    IntervalThread(name="5 second", interval=5, target=work_imitation).start()
    IntervalThread(name="3 second", interval=3, target=work_imitation).start()
    IntervalThread(name="1 second", interval=1, target=work_imitation).start()
