import logging
import time

from .baseclient import BaseClient

log = logging.getLogger("mqtt-test")


class TestClient(BaseClient):
    def create_function_map(self):
        return dict(abc=self.abc, msg=self.xyz,)

    def abc(self, message):
        log.info("abc: %s", message)

    def xyz(self, message):
        log.info("x")
        time.sleep(1)
        log.info("y")
        time.sleep(1)
        log.info("z")
