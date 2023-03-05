from typing import Protocol,Iterable,TypeVar,Sequence,Generic,List,Callable,Set,Deque,Dict,Any,Optional
from heapq import heappush,heappop

T = TypeVar("T")
def linear_contains(iterable: Iterable[T],key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar("C",bound="Comparable")
class Comparable(Protocol):
    def __gt__(self: C, other:C) -> bool:
        return (not self < other) and self != other

    def __le__(self:C, other:C) -> bool:
        return self < other or self == other

    def __ge__(self:C, other:C) -> bool:
        return not self < other

def binary_contains(sequence:Sequence[C],key:C) -> bool:
    low: int = 0
    hight: int = len(sequence) - 1
    while low <= hight:
        mid: int = (low + hight) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            hight = mid - 1
        else:
            return True
    return True


if __name__ == "__main__":
    print(linear_contains([1,5,15,15,15,20],5))
    print(binary_contains(["a","d","e","f","z"],"f"))


