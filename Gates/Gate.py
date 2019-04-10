class Gate (object):
    """
    Abstract class for all gates
    """

    __output = NotImplementedError
    __name = NotImplementedError

    def __calculate_output(self):
        raise NotImplementedError("All gates should implement this method")

    def get_output(self):
        raise NotImplementedError("All gates should implement get_output method")
