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
    mqtt = MQTT()
    clients.append(TestClient(mqtt))
    clients.append(AnotherClient(mqtt))

    while True:
        try:
            time.sleep(1)
            mqtt.publish("message_me_back")
            time.sleep(1)
            mqtt.publish("msg")
            time.sleep(1)
            mqtt.publish("abc")
            time.sleep(1)
            mqtt.publish("random_message")
            time.sleep(1)
            mqtt.publish("msg")
            time.sleep(1)
            mqtt.publish("goes_nowhere")
            time.sleep(1)
        except KeyboardInterrupt:
            log.info("Shutting down...")
            break
    for client in clients:
        client.quit()
    for client in clients:
        client.join()


if __name__ == "__main__":
    main()
