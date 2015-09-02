import re


class Stringcalculator(object):
    @staticmethod
    def add(str):
        if str == "":
            return 0
        elif not re.search(",", str):
            return int(str)
        else:
            components = str.split(",")
            return(int(components[0]) + int(components[1]))
