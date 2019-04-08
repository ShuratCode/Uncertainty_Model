class Gate:
    """
    Abstract class for all gates
    """

    def __calculate_output(self):
        raise NotImplementedError("All gates should implement this method")

    def get_output(self):
        raise NotImplementedError("All gates should implement get_output method")