from .Record import Record
from .Field import Field
from .TableSchema import TableSchema


class Table:
    def __init__(self, table_schema):
        self.name = table_schema.table_name
        self.columns = {}
        
        for field_name in table_schema.field_names:
            self.columns.update({field_name: []})
    
    def add_record(self, record):
        for field in record.fields:
            self.columns[field.name].append(field.value)

    def get_column_names(self):
        return list(self.columns.keys())

    def get_record_count(self):
        return len(self.columns[self.get_column_names()[0]])

    def get_records(self):
        records = []
        for i in range(self.get_record_count()):
            record = Record()
            for column_name in self.get_column_names():
                record.add_field(Field(column_name, self.columns[column_name][i]))
            records.append(record)
        return records
