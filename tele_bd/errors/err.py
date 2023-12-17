from tele_bd.config import SEPARATOR


class TableNotChosen(ValueError):
    def __init__(self, message="Table not formally chosen, re-start"):
        """
        Error indicates that table is not chosen
        :ivar message: error message
        :vartype message: str
        """
        super().__init__()
        self.msgfmt = message


class DataIsNoneOrNotTuple(ValueError):
    def __init__(self, message="Data is None or Value is not tuple"):
        """
        Error indicates that data type is None or Tuple
        :ivar message: error message
        :vartype message: str
        """
        super().__init__()
        self.msgfmt = message


class SeparatorError(ValueError):
    def __init__(self):
        """
        Error indicates that Separator does not equal to separator from config file
        """
        super().__init__()
        self.msgfmt = f"Separator does not equal to {SEPARATOR}"
