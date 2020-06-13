import logging
import queue
import threading

log = logging.getLogger("mqtt-test")


class BaseClient:
    def __init__(self, mqtt):
        self.mqtt = mqtt
        self.queue = queue.Queue()
        self.message_to_function = self.create_function_map()
        self._quit = threading.Event()
        self.worker = threading.Thread(target=self.do_work, daemon=True)
        self.worker.start()

    def on_message(self, message):
        if not self._quit.is_set() and message in self.message_to_function.keys():
            log.debug("%s received message: %s", self.__class__.__name__, message)
            self.queue.put(message)

    def send_message(self, message):
        if not self._quit.is_set():
            log.debug("%s sending message: %s", self.__class__.__name__, message)
            self.mqtt.publish(message)

    def do_work(self):
        while not self._quit.is_set():
            try:
                message = self.queue.get(timeout=0.1)
            except queue.Empty:
                continue
            log.debug("%s starting work on message: %s", self.__class__.__name__, message)
            func = self.message_to_function.get(message)
            func(message)
            log.debug("%s finished working on message: %s", self.__class__.__name__, message)
            self.queue.task_done()

    def quit(self):
        self._quit.set()

    def join(self):
        self.worker.join()

    def create_function_map(self) -> dict:
        raise NotImplementedError()
