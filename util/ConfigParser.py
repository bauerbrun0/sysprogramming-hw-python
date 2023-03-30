from abc import ABC, abstractmethod


class ConfigParser(ABC):
    @abstractmethod
    def parse(self, config_file_name):
        pass

class ConfigFileNotFound(Exception):
    pass

class InvalidConfigFile(Exception):
    pass
