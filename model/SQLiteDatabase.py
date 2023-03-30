import sqlite3
from .Database import *
from .TableSchema import *


class SQLiteDatabase(Database):
    def __init__(self, path, initial_table):
        super().__init__()
        self.path = path
        
        self._init_table(initial_table)

    def _check_database_exists(self):
        # SQLite creates database file automatically
        pass

    def _create_database(self):
        # SQLite creates database file automatically
        pass

    def _init_table(self, table_schema):
        if not self._check_table_exists(table_schema.table_name):
            self._create_table(table_schema)
            return
        if not self._check_table_schema_matches(table_schema.table_name, table_schema):
            raise InvalidDatabase

    def _check_table_exists(self, table_name):
        cursor = self._connect()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        self._disconnect()
        return result is not None

    def _check_table_schema_matches(self, table_name, table_schema):
        column_names = self.get_column_names_of_table(table_name)
        db_schema = TableSchema(table_name, column_names)
        return db_schema == table_schema

    def get_column_names_of_table(self, table_name):
        cursor = self._connect()
        cursor.execute("PRAGMA table_info(" + table_name + ")")
        result = cursor.fetchall()
        self._disconnect()
        return [column[1] for column in result]
    
    def _create_table(self, table_schema):
        cursor = self._connect()
        query_string = "CREATE TABLE " + table_schema.table_name + " (" + ", ".join([field_name + " TEXT" for field_name in table_schema.field_names]) + ")"
        cursor.execute(query_string)
        self._commit()
        self._disconnect()

    def store_records(self, table_name, records):
        cursor = self._connect()
        for record in records:
            values = [field.value for field in record.fields]
            field_names = [field.name for field in record.fields]
            cursor.execute("INSERT INTO " + table_name + " (" + ", ".join(field_names) + ") VALUES (" + ", ".join(["?"] * len(values)) + ")", values)
        self._commit()
        self._disconnect()

    def _connect(self):
        self.connection = sqlite3.connect(self.path)
        cursor = self.connection.cursor()
        return cursor

    def _commit(self):
        self.connection.commit()

    def _disconnect(self):
        self.connection.close()
