from abc import ABC, abstractmethod


class LoggerInterface(ABC):
    """ LoggerInterface class provides an interface for logging.
    """

    @abstractmethod
    def log_debug(self, message: str) -> None:
        """ Log debug message.
        :param message: Message to log.
        """
        pass

    @abstractmethod
    def log_info(self, message: str) -> None:
        """ Log debug message.
        :param message: Message to log.
        """
        pass

    @abstractmethod
    def log_warning(self, message: str) -> None:
        """ Log debug message.
        :param message: Message to log.
        """
        pass

    @abstractmethod
    def log_error(self, message: str) -> None:
        """ Log debug message.
        :param message: Message to log.
        """
        pass

    @abstractmethod
    def log_critical(self, message: str) -> None:
        """ Log critical message.
        :param message: Message to log.
        """
        pass

    @abstractmethod
    def log_exception(self, message: str) -> None:
        """ Log exception message with exception info.
        :param message: Message to log.
        """
        pass

    @abstractmethod
    def log_debugs(self, *args, **kwargs) -> None:
        """ Log exception message with exception info.
        :param message: Message to log.
        """
        pass

    @abstractmethod
    def log_infos(self, *args, **kwargs) -> None:
        """ Log debug message.
        :param message: Message to log.
        """
        pass

    @abstractmethod
    def log_warnings(self, *args, **kwargs) -> None:
        """ Log debug message.
        :param message: Message to log.
        """
        pass

    @abstractmethod
    def log_errors(self, *args, **kwargs) -> None:
        """ Log debug message.
        :param message: Message to log.
        """
        pass

    @abstractmethod
    def log_critics(self, *args, **kwargs) -> None:
        """ Log critical message.
        :param message: Message to log.
        """
        pass

    @abstractmethod
    def log_exceptions(self, *args, **kwargs) -> None:
        """ Log exception message with exception info.
        :param message: Message to log.
        """
        pass