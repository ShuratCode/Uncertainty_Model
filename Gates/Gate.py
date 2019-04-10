class Gate (object):
    """
    Abstract class for all gates
    """

    output = NotImplementedError
    name = NotImplementedError
    inputs = NotImplementedError

    def calculate_output(self):
        raise NotImplementedError("All gates should implement this method")

    def get_output(self):
        raise NotImplementedError("All gates should implement get_output method")
