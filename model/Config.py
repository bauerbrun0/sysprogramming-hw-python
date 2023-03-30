class Config:
    def __init__(self, output_file, data_file, table_name, fields):
        self.output_file = output_file
        self.data_file = data_file
        self.table_name = table_name
        self.fields = fields

class Field:
    def __init__(self, name, label):
        self.name = name
        self.label = label
