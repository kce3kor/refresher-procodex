from procodex.config import LOG_DIR, LOG_FORMAT
from loguru import logger

# Specifying Logger Format


# prevent loguru from printing the logs in the console
logger.remove()

import sys

logger.add(sys.stderr, format=LOG_FORMAT, backtrace=True, diagnose=True)
# Sink Sepcifications

logger.add(
    f"{LOG_DIR}/" + "{time}.log",
    format=LOG_FORMAT,
    rotation="5 MB",
    retention="120 Days",
    backtrace=True,
    diagnose=True,
)
