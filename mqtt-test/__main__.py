import logging
import time
from .clients.anotherclient import AnotherClient
from .clients.testclient import TestClient

log = logging.getLogger("mqtt-test")

clients = []


# This is just a dummy you should be able to replace
class MQTT:
    def on_message(self, message):
        for client in clients:
            client.on_message(message)

    def publish(self, message):
        self.on_message(message)


def main():
    global clients
    mqtt = MQTT()
    clients.append(TestClient(mqtt))
    clients.append(AnotherClient(mqtt))

    while True:
        try:
            time.sleep(1)
            mqtt.on_message("message_me_back")
            time.sleep(1)
            mqtt.on_message("msg")
            time.sleep(1)
            mqtt.on_message("abc")
            time.sleep(1)
            mqtt.on_message("random_message")
            time.sleep(1)
            mqtt.on_message("msg")
            time.sleep(1)
            mqtt.on_message("goes_nowhere")
            time.sleep(1)
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    main()
