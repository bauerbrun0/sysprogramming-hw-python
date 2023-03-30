from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def _check_database_exists(self):
        pass

    @abstractmethod
    def _create_database(self):
        pass

    @abstractmethod
    def _init_table(self, table_schema):
        pass

    @abstractmethod
    def _check_table_exists(self, table_name):
        pass

    @abstractmethod
    def _check_table_schema_matches(self, table_name, table_schema):
        pass
    
    @abstractmethod
    def _create_table(self, table_schema):
        pass
    
    @abstractmethod
    def store_records(self, table_name, records):
        pass

class InvalidDatabase(Exception):
    pass
