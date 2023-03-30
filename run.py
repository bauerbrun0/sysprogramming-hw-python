import argparse
import os
from controller.Controller import Controller
from view.PyQtView import PyQtView


def main_():
    DEFAULT_CONFIG_FILE = "config.yaml"

    args = parse_args()
    if args.config:
        config_file_path = os.path.realpath(args.config)
    else:
        config_file_path = os.path.realpath(DEFAULT_CONFIG_FILE)

    controller = Controller(PyQtView())
    controller.start(config_file_path)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Path to config file")
    return parser.parse_args()


if __name__ == "__main__":
    main_()
