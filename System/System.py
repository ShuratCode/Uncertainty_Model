import os.path
import re

"""
Representing a system base on sys file.
"""

system_file_type = '.sys'


class System:
    system_file_type = '.sys'

    def __init__(self, path_to_file: str):
        if os.path.isfile(path_to_file) and system_file_type in path_to_file:
            file = open(path_to_file, 'r')
            file_content = self.__read_file(file)
            index_of_input = self.__get_system_name(file_content)


    @staticmethod
    def __read_file(file):
        """
        Read the file content and connect it to a single string and split by '.' delimiter
        :param file: file object of the system model
        :return: list of strings. each cell in the list is a parameter of the model: system name, inputs, outputs, gates
        """
        file_content = ""
        for line in file:
            line = line.strip()
            file_content += line
        file_content = file_content.split('.')
        return file_content

    def __get_system_name(self, file_content: list):
        """
        get the system name from list of the file content
        :param file_content: list of the parameters of the system model. the output of __read_file method
        :return: the index of the next parameter in the list - inputs
        """
        if file_content[0] != "":
            self.system_name = file_content[0]
            return 1
        else:
            self.system_name = file_content[1]
            return 2






