from FS import FS
import re
import sys

class TestsArguments:

    def __init__(self):
        self.fs = FS()
        self.class_choosed = self.get_class()
        self.method_choosed = self.get_method()


    def get_class(self):
        try:
            first_argument_given = sys.argv[1]
        except:
            raise Exception("The first argument, that must be the class name, has not been setted.")

        tests_files = self.fs.get_file_list("Tests")
        classes_allowed = self.filter_valid_files_from_tests(tests_files)
        if not first_argument_given in classes_allowed:
            raise("The class given is not a valid choosen.")

        return first_argument_given


    def get_method(self):
        try:
            return sys.argv[2]
        except:
            raise Exception("The first argument, that must be the method name, has not been setted.")


    def filter_valid_files_from_tests(self, raw_list) -> list:
        invalid_occurrences = ["__pycache__", "TestsArguments.py"]

        for invalid in invalid_occurrences:
            print("The invalid is " + invalid)
            raw_list.remove(invalid)

        filtered_list = []
        for item_list in raw_list:

            filtered_list.append(item_list)

        # print(raw_list)
        # raw_list.remove("TestsArguments.py")
        # print(raw_list)

        return raw_list
