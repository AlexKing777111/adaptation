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
        while True:
            print(
                f"---Поток {threading.currentThread().name} начал работу.---"
            )
            time.sleep(randint(1, 10))
            print(
                f"---Поток {threading.currentThread().name} закончил работу.---"
            )
            time.sleep(self.interval)


if __name__ == "__main__":
    IntervalThread(interval=10).start()
    IntervalThread(name="Ivan").start()
