__author__ = "Bogdan Gladyshev"
__copyright__ = "Copyright 2017, Bogdan Gladyshev"
__credits__ = ["Bogdan Gladyshev"]
__license__ = "MIT"
__version__ = "0.1.0"
__maintainer__ = "Bogdan Gladyshev"
__email__ = "siredvin.dark@gmail.com"
__status__ = "Production"

__all__ = ['ComparationMock']


class ComparationMock:

    __slots__ = ['_always_max']

    def __init__(self, always_max: bool = True) -> None:
        self._always_max = always_max

    def __le__(self, other) -> bool:
        return not self._always_max

    def __lt__(self, other) -> bool:
        return not self._always_max

    def __eq__(self, other) -> bool:
        return False

    def __ge__(self, other) -> bool:
        return self._always_max

    def __gt__(self, other) -> bool:
        return self._always_max
