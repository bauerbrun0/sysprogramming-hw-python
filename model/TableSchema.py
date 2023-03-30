class TableSchema:
    def __init__(self, table_name, field_names):
        self.table_name = table_name
        self.field_names = field_names

    def __eq__(self, other):
        if self.table_name != other.table_name:
            return False

        if len(self.field_names) != len(other.field_names):
            return False

        for field_name in self.field_names:
            if field_name not in other.field_names:
                return False

        return True
