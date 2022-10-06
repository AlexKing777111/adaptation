import threading
import time

# сигнал завершения работы потока.
stop_event = threading.Event()

# блокировка доступа к списку потоков.
tasks_lock = threading.Lock()

# Список потоков, ожидающих выполнения.
task_list = []


class ThreadByInterval(threading.Thread):
    def __init__(self, name, timeout):
        super().__init__()
        self.name = name
        self.timeout = timeout
        # Ожидаемое время запуска задачи.
        # Задача запускается сразу при создании.
        self.time = time.time()

    def run(self):
        # Имитация работы.
        print("Running :", self.name, " at ", int(time.time()))
        # Имитация работы.

        # Ожидаемое время запуска задачи.
        # Следующий запуск = время окончания работы + таймаут.
        self.time = time.time() + self.timeout

        # Вернули поток в список ожидания.
        tasks_lock.acquire()
        next_task = ThreadByInterval(self.name, self.timeout)
        next_task.time = self.time
        task_list.append(next_task)
        tasks_lock.release()

        # Сигнал об окончании работы потока.
        stop_event.set()


task_list.extend(
    [
        ThreadByInterval("thread 1", 10),
        ThreadByInterval("thread 2", 1),
        ThreadByInterval("thread 3", 2),
        ThreadByInterval("thread 4", 5),
    ]
)


while True:
    # Текущее время.
    cureent_time = time.time()

    # Блокируем список задач для запуска.
    # Никакая другая задача не будет обращаться с списку задач, пока мы не закончим.
    tasks_lock.acquire()
    # Сюда попадёт ближайшее время следующего запуска задачи из списка.
    next_time = None
    # Новый список задач.
    new_list = []

    # Запускаем задачи ели пришло время.
    for task in task_list:
        # Проверяем пора ли запускать задачу.
        if task.time <= cureent_time:
            # Пришло время запуска
            task.start()
        else:
            # Ещё не время - выясняем сколько осталось.
            # И корректируем ремя ближайшего запуска.
            if next_time is None or next_time > task.time:
                next_time = task.time
            # Добавляем задачу в список ожидания запуска.
            new_list.append(task)

    # Получили новый список задач.
    # Кому пишло время - запущены.
    # Остальные в этом списке.
    task_list = new_list
    # Освобождем список задач.
    tasks_lock.release()

    # Ждём, когда закончит работу какой либо поток или
    # подойдёт время запуска потока.
    if next_time is None:
        # next_time == None если запущены все задачи.
        # Нет ожидающих.
        # Просто ждём когда кто нить завершиться.
        stop_event.wait()
    else:
        # Есть задачи в списке ожидания.
        # Ближайшую надо запускать через next_time - cureent_time секунд.
        # Ждём либо next_time - cureent_time секунд, либо завершения задачи.
        stop_event.wait(next_time - cureent_time)
    stop_event.clear()
