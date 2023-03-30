import os
import json
from .Database import *
from .TableSchema import *


class JSONDatabase(Database):
    def __init__(self, path, initial_table):
        super().__init__()
        self.path = path

        # creating database if it doesn't exist
        if not self._check_database_exists():
            self._create_database()
        else:
            self._check_database()
        
        # setting up initial table
        self._init_table(initial_table)


    def _check_database_exists(self):
        return os.path.exists(self.path)

    def _create_database(self):
        initial_data = []
        json_data = json.dumps(initial_data)
        
        os.makedirs(os.path.dirname(self.path), exist_ok=True)

        db_file = open(self.path, "w")
        db_file.write(json_data)
        db_file.close()

    def _check_database(self):
        db_file = open(self.path, "r")
        json_data = db_file.read()
        db_file.close()
        data = json.loads(json_data)

        if not isinstance(data, list):
            raise InvalidDatabase

    def _init_table(self, table_schema):
        self._check_table_schema_matches(table_schema.table_name, table_schema)

    def _check_table_exists(self, table_name):
        pass

    def _check_table_schema_matches(self, table_name, table_schema):
        db_file = open(self.path, "r")
        json_data = db_file.read()
        db_file.close()
        data = json.loads(json_data)

        if len(data) == 0:
            return
        
        for record in data:
            if not isinstance(record, dict):
                raise InvalidDatabase
            record_schema = TableSchema(table_name, list(record.keys()))
            if record_schema != table_schema:
                raise InvalidDatabase

    def _create_table(self, table_schema):
        pass
    
    def store_records(self, table_name, records):
        # table_name is not used in JSONDatabase
        db_file = open(self.path, "r+")
        json_data = db_file.read()
        data = json.loads(json_data)
        for record in records:
            data.append({field.name: field.value for field in record.fields})
        json_data = json.dumps(data, indent=4)
        db_file.seek(0)
        db_file.write(json_data)
        db_file.close()
