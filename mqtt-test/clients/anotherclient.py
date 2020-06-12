import logging
import time

from .baseclient import BaseClient

log = logging.getLogger("mqtt-test")


class AnotherClient(BaseClient):
    def create_function_map(self):
        return dict(
            message_me_back=self.message_sending_function, ok_i_gotcha=self.received,
        )

    def message_sending_function(self, message):
        log.info(message)
        time.sleep(3)
        log.info("messaging you back now")
        self.send_message("ok_i_gotcha")

    def received(self, message):
        log.info(message)
        log.info("ok i got your message")
