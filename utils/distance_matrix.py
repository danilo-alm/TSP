import numpy as np

class DistanceMatrix:
    __default_dtype = np.uint16

    @staticmethod
    def from_text(text, dtype=None):
        return np.array(
            [[float(x) for x in row.split()] for row in text.splitlines() if row != ''],
            dtype=dtype or DistanceMatrix.__default_dtype
        )

    @staticmethod
    def from_text_file(filepath, dtype=None):
        with open(filepath, 'r') as rf:
            return DistanceMatrix.from_text(rf.read(), dtype)
    
    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
