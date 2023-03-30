import yaml
import os
from .ConfigParser import *
from model.Config import Config, Field


class YAMLConfigParser(ConfigParser):
    def parse(self, config_file_path):
        try:
            config_file = open(config_file_path, 'r')
        except FileNotFoundError:
            raise ConfigFileNotFound

        try:
            config = yaml.safe_load(config_file)
        except yaml.YAMLError:
            raise InvalidConfigFile
        finally:
            config_file.close()

        try:
            output_file = os.path.realpath(config['output_file'])
            data_file = os.path.realpath(config['data_file'])
            table_name = config['table_name']
            fields = config['fields']

            fields = [Field(field['field_name'], field['label']) for field in fields]
        except KeyError:
            raise InvalidConfigFile

        return Config(output_file, data_file, table_name, fields)
