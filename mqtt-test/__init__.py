import logging
import sys

log = logging.getLogger("mqtt-test")
log.setLevel(logging.INFO)

log_handler = logging.StreamHandler(sys.stdout)
log_handler.setLevel(logging.INFO)
log_formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
log_handler.setFormatter(log_formatter)
log.addHandler(log_handler)
