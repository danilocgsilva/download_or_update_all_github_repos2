from FS import FS
import importlib
from inspect import getmembers, isfunction
from Environment import Environment
import re
import sys

class TestsArguments:

    def __init__(self):
        self.fs = FS()
        self.class_choosed = self.get_class()
        self.method_choosed = self.get_method()


    def get_class(self) -> str:
        try:
            first_argument_given = sys.argv[1]
        except:
            raise Exception("The first argument, that must be the class name, has not been setted.")

        tests_files = self.fs.get_file_list("Tests")
        classes_allowed = self.filter_valid_files_from_tests(tests_files)
        if not first_argument_given in classes_allowed:
            raise Exception("The class given is not a valid choosen.")

        return first_argument_given


    def get_method(self) -> str:
        try:
            second_argument_given = sys.argv[2]
        except:
            raise Exception("The second argument, that must be the method name, has not been setted.")

        choosed_class_instance = importlib.import_module(self.class_choosed)
        env = Environment()
        print(dir(env))
        print("---")
        print(dir(choosed_class_instance))

        return second_argument_given


    def filter_valid_files_from_tests(self, raw_list) -> list:
        invalid_occurrences = ["__pycache__", "TestsArguments.py"]

        for invalid in invalid_occurrences:
            raw_list.remove(invalid)

        filtered_list = []
        for item_list in raw_list:
            if re.search('.py$', item_list):
                item_list = item_list[:(len(item_list) - 3)]
            filtered_list.append(item_list)

        return filtered_list
