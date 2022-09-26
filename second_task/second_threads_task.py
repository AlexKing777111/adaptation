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
    print(
        f"---Поток {threading.currentThread().name} "
        f"начал работу в {datetime.now().strftime('%H:%M:%S')}---"
    )
    time.sleep(randint(1, 10))
    print(
        f"---Поток {threading.currentThread().name} "
        f"закончил работу в {datetime.now().strftime('%H:%M:%S')}---"
    )
    time_stamp[
        round(time.time()) + threading.current_thread().interval
    ] = IntervalThread(
        name=threading.current_thread().name,
        interval=threading.current_thread().interval,
        target=work_imitation,
    )


if __name__ == "__main__":
    time_stamp = {}
    IntervalThread(name="first", interval=1, target=work_imitation).start()
    IntervalThread(name="second", interval=5, target=work_imitation).start()
    IntervalThread(name="third", interval=10, target=work_imitation).start()
    while True:
        time_now = round(time.time())
        if time_now in time_stamp:
            thr = time_stamp.pop(time_now)
            thr.start()
