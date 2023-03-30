import sys
from util.YAMLConfigParser import YAMLConfigParser
from util.ConfigParser import ConfigFileNotFound, InvalidConfigFile
from model.Field import Field
from model.Record import Record
from model.Table import Table
from model.TableSchema import TableSchema
from model.JSONDatabase import JSONDatabase
from model.SQLiteDatabase import SQLiteDatabase
from model.Database import InvalidDatabase
from view.View import View


class Controller:
    def __init__(self, view: View):
        self.view = view

    def start(self, config_file_path):
        self.view.setup(self)

        self._load_config(config_file_path)
        if self.config is None:
            sys.exit(1)

        self.table_schema = TableSchema(self.config.table_name, [field.name for field in self.config.fields])
        self.table = Table(self.table_schema)

        self.init_databases()
        if len(self.databases) == 0:
            sys.exit(1)

        self.view.start()
        

    def _load_config(self, config_file_path):
        yaml_config_parser = YAMLConfigParser()

        try:
            self.config = yaml_config_parser.parse(config_file_path)
        except ConfigFileNotFound:
            self.view.show_dialog("Config file not found", "error")
            self.config = None
        except InvalidConfigFile:
            self.view.show_dialog("Invalid config file", "error")
            self.config = None

    def init_databases(self):
        databases = []
        initial_table = self.table_schema
        try:
            json_database = JSONDatabase(self.config.output_file, initial_table)
            sqlite_database = SQLiteDatabase(self.config.data_file, initial_table)
            databases.append(json_database)
            databases.append(sqlite_database)
        except InvalidDatabase:
            self.view.show_dialog("Invalid database", "error")
        
        self.databases = databases

    def load_fields_to_layout(self):
        for field in self.config.fields:
            self.view.add_field_to_layout(field.name, field.label)

    def handle_click_save(self):
        if not self._check_field_inputs():
            return

        record = Record()
        for field in self.view.get_fields():
            record.add_field(Field(field.field_name, field.get_input_text()))
        
        self.table.add_record(record)
        self.view.clear_fields()
        
    def _check_field_inputs(self):
        for field in self.view.get_fields():
            if field.get_input_text() == "":
                self.view.show_dialog("Field '" + field.label + "' is empty", "error")
                return False
        return True

    def handle_click_exit(self):
        if self.table.get_record_count() == 0:
            self.view.close()
            return

        for database in self.databases:
            database.store_records(self.table.name, self.table.get_records())
        self.view.show_dialog("Records saved", "info")
        self.view.close()

        

