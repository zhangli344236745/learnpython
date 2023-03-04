from typing import TypeVar,Generic,List

T = TypeVar("T")
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._conatner: List[T] = []

    def push(self,item: T) -> None:
        self._conatner.append(item)

    def pop(self) -> T:
        return self._conatner.pop()

    def __repr__(self) -> str:
        return repr(self._conatner)

num: int =3
towa: Stack[int] = Stack()
for i in range(1,num+1):
    towa.push(i)