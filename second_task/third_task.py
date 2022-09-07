import threading
import time
from queue import Queue
from random import randint


def message_maker():
    i = 1
    while i <= 20:
        yield i
        i += 1


def message_processing(q):
    while True:
        check = q.get()
        time.sleep(randint(1, 10))
        print(f"Сообщение {check} обработано.")
        q.task_done()


if __name__ == "__main__":
    start_time = time.time()
    q = Queue()
    for i in message_maker():
        q.put(i)
    thread1 = threading.Thread(
        target=message_processing, args=(q,), daemon=True
    )
    thread2 = threading.Thread(
        target=message_processing, args=(q,), daemon=True
    )
    thread3 = threading.Thread(
        target=message_processing, args=(q,), daemon=True
    )
    thread1.start()
    time.sleep(0.5)
    thread2.start()
    time.sleep(0.5)
    thread3.start()
    q.join()
    print("Все сообщения обработаны.")
    print(f"Время выполнения программы - {time.time() - start_time} секунд.")
