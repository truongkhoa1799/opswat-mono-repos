from .default_logger import DefaultLogger
from .logger import LoggerInterface


class LoggerFactory:
    _instances = {}

    @staticmethod
    def get_logger() -> LoggerInterface:
        if "default_logger" in LoggerFactory._instances:
            return LoggerFactory._instances['default_logger']
        else:
            LoggerFactory._instances['default_logger'] = DefaultLogger()

        return LoggerFactory._instances['default_logger']