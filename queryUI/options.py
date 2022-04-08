
class Options:
    padding = {"ipadx": 5, "ipady": 5, "padx": 3, "pady": 3}
    padding_tight = {"ipadx": 2, "ipady": 2, "padx": 1, "pady": 1}
    padding_title = {"padx": (2, 15), "pady": (3,0)}
    

    def __init__(self, num_cols=1):
        self._num_cols = num_cols
        self.full_row = {"columnspan": num_cols}
