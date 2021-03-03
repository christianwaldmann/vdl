import sys
import logging
from pathlib import Path


class Log:
    logger = None

    @staticmethod
    def Init():
        Log.logger = logging.getLogger("Log")
        Log.logger.setLevel(logging.DEBUG)

        format = "%(asctime)s | %(message)s"
        formatter = logging.Formatter(format)

        Path(sys.path[0]).joinpath("logs").mkdir(parents=True, exist_ok=True)
        filepath = Path(sys.path[0]).joinpath("logs/logs.log")
        handler = logging.FileHandler(filepath, encoding="utf-8")
        handler.setFormatter(formatter)

        Log.logger.addHandler(handler)

    @staticmethod
    def Trace(message):
        Log.logger.debug(message)

    @staticmethod
    def Info(message):
        Log.logger.info(message)

    @staticmethod
    def Warn(message):
        Log.logger.warn(message)

    @staticmethod
    def Error(message):
        Log.logger.error(message)
