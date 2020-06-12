import threading
import queue


class BaseClient:
    def __init__(self, mqtt):
        self.mqtt = mqtt
        self.queue = queue.Queue()
        self.message_to_function = self.create_function_map()

        self.worker = threading.Thread(target=self.do_work, daemon=True)
        self.worker.start()

    def on_message(self, message):
        if message in self.message_to_function.keys():
            self.queue.put(message)

    def send_message(self, message):
        self.mqtt.publish(message)

    def do_work(self):
        while True:
            message = self.queue.get()
            func = self.message_to_function.get(message)
            func(message)

    def create_function_map(self) -> dict:
        raise NotImplementedError()
