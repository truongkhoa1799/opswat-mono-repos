import inspect
import os
import logging
import logging.config
import yaml

from src.common import Config
from src.insfra.logger.logger import LoggerInterface


class InfoFilter(logging.Filter):
    def __init__(self):
        super().__init__()

    def filter(self, record):
        return record.levelno == logging.INFO


class ErrorFilter(logging.Filter):
    def __init__(self):
        super().__init__()

    def filter(self, record):
        return record.levelno >= logging.ERROR


class DefaultLogger(LoggerInterface):
    _logger: logging.Logger = None

    def __init__(self, level: int = logging.DEBUG):
        conf = Config()
        with open(conf.get('LOGGER_CONFIG'), 'r') as f:
            config = yaml.safe_load(f.read())
            logging.config.dictConfig(config)

        # Create a custom self._logger
        self._logger = logging.getLogger(conf.get('ENV'))
        self._logger.setLevel(level)

    def log_debug(self, message: str) -> None:
        """ Log debug message.
        :param message: Message to log.
        """
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = os.path.basename(module.__file__)

        message = f"[{filename}]\t[{message}]"
        self._logger.debug(message)

    def log_info(self, message: str) -> None:
        """ Log info message.
        :param message: Message to log.
        """
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = os.path.basename(module.__file__)

        message = f"[{filename}]\t[{message}]"
        self._logger.info(message)

    def log_warning(self, message: str) -> None:
        """ Log warning message.
        :param message: Message to log.
        """
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = os.path.basename(module.__file__)

        message = f"[{filename}]\t[{message}]"
        self._logger.warning(message)

    def log_error(self, message: str) -> None:
        """ Log error message.
        :param message: Message to log.
        """
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = os.path.basename(module.__file__)

        message = f"[{filename}]\t[{message}]"
        self._logger.error(message)

    def log_critical(self, message: str) -> None:
        """ Log critical message.
        :param message: Message to log.
        """
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = os.path.basename(module.__file__)

        message = f"[{filename}]\t[{message}]"
        self._logger.critical(message)

    def log_exception(self, message: str) -> None:
        """ Log exception message with exception info.
        :param message: Message to log.
        """
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = os.path.basename(module.__file__)

        message = f"[{filename}]\t[{message}]"
        self._logger.exception(message)

    # exc_info = True: Capturing Stack Traces
    def log_debugs(self, *args, **kwargs) -> None:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = os.path.basename(module.__file__)

        message = ",".join(list(args))
        message = f"[{filename}]\t[{message}]"
        self._logger.debug(message)

    def log_infos(self, *args, **kwargs) -> None:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = os.path.basename(module.__file__)

        message = ",".join(list(args))
        message = f"[{filename}]\t[{message}]"
        self._logger.info(message)

    def log_warnings(self, *args, **kwargs) -> None:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = os.path.basename(module.__file__)

        message = ",".join(list(args))
        message = f"[{filename}]\t[{message}]"
        self._logger.warning(message)

    def log_errors(self, *args, **kwargs) -> None:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = os.path.basename(module.__file__)

        message = ",".join(list(args))
        message = f"[{filename}]\t[{message}]"
        self._logger.error(message, exc_info=True)

    def log_critics(self, *args, **kwargs) -> None:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = os.path.basename(module.__file__)

        message = ",".join(list(args))
        message = f"[{filename}]\t[{message}]"
        self._logger.critical(message, exc_info=True)

    def log_exceptions(self, *args, **kwargs) -> None:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        filename = os.path.basename(module.__file__)

        message = ",".join(list(args))
        message = f"[{filename}]\t[{message}]"
        self._logger.exception(message, exc_info=True)
