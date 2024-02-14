import json


class DataController:
    def __init__(self, data_file):
        self.__data_file = data_file
        self.__old = None
        self.__data = None  # type: dict | list | str | None
        self.__load_data()

    def __load_data(self):
        with open(self.__data_file, 'r') as f:
            self.__data = json.load(f)

    def save(self):
        with open(self.__data_file, 'w') as f:
            json.dump(self.__data, f)

    def get_data(self):
        return self.__data

    def overwrite_data(self, data):
        self.__old = self.__data
        self.__data = data

    def undo_overwrite(self):
        self.__data = self.__old
