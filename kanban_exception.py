'''
Module for handling exceptions

'''


class Name_repetition(Exception):
    pass


class Wrong_input_str(Exception):
    message = "\n\nArgument should be of type str \n"
    def __init__(self):
        super().__init__(self.message)


class Last_Column(Exception):
    message = "\n\nAssignment is in last column\n"
    def __init__(self):
        super().__init__(self.message)


                