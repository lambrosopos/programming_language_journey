import pytest

class SparseArray:
    def __init__(self, array: list[int], size: int):
        self.size = size
        self.sparse_array = array

    @property
    def sparse_array(self):
        return self._sparse_array

    @sparse_array.setter
    def sparse_array(self, array: list[int]):
        sparse_dict = {}
        for i, v in enumerate(array):
            if v == 0:
                continue
            sparse_dict[i] = v

        self._sparse_array = sparse_dict

    def check_bounds(self, idx: int):
        if 0 <= idx < self.size:
            return True
        else:
            raise IndexError


    def get(self, idx: int):
        if self.check_bounds(idx):
            return self._sparse_array.get(idx, 0)

    def set(self, idx: int, val: int):
        if self.check_bounds(idx):
            self._sparse_array[idx] = val


def test_p134_1():
    arr = SparseArray([0, 0, 0], 5)

    assert arr.get(0) == 0
    assert arr.get(3) == 0

    with pytest.raises(IndexError):
        assert arr.get(-1)
        assert arr.get(-1, 0)
        assert arr.get(5)
        assert arr.set(5, 0)

    arr.set(0, 1)
    assert arr.get(0) == 1

    arr.set(4, 1)
    assert arr.get(4) == 1

def main():
    test_p134_1()
