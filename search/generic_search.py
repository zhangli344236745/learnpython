from __future__ import annotations
from typing import Protocol,Iterable,TypeVar,Sequence,Generic,List,Callable,Set,Deque,Dict,Any,Optional
from heapq import heappush,heappop

T = TypeVar("T")

def linear_contains(iterable: Iterable[T],key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self,item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

class Node(Generic[T]):
    def __init__(self , state:T, parant: Optional[Node],cost: float = 0.0,heuristic: float = 0.0) -> None:
        self.state = state
        self.parent:Optional[Node] = parant
        self.cost: float = cost
        self.heuritic = heuristic

    def __lt__(self, other:Node) -> bool:
        return (self.cost + self.heuritic)< (other.cost + other.heuritic)

def dfs(initial: T,goal_test:Callable[[T],bool],successors:Callable[[T],List[T]]) -> Optional[Node[T]]:
    frontier : Stack[Node[T]] = Stack()
    frontier.push(Node(initial,None))
    explored: Set[T] = {initial}
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child,current_node))
    return None

class Queue(Generic[T]):
    def __init__(self) -> None:
        self.__container: Deque[T] = Deque()
    @property
    def empty(self) -> bool:
        return not self.__container

    def pop(self) -> T:
        return self.__container.popleft()

    def push(self,item:T) -> None:
        self.__container.append(item)

    def __repr__(self) -> str:
        return repr(self.__container)

def bfs(inital:T,goal_test:Callable[[T],bool],successors:Callable[[T],List[T]]) -> Optional[Node[T]]:
    frozenser: Queue[Node[T]] = Queue()
    frozenser.push(Node(inital,None))
    explored :Set[T] = {inital}
    while not frozenser.empty:
        current_node:Node[T] = frozenser.pop()
        current_state: T = current_node.state

        if goal_test(current_state):
            return current_node

        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frozenser.push(Node(child,current_node))
    return None

class PriorityQueue(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self,item:T) -> None:
        heappush(self._container,item)

    def pop(self) -> T:
        return heappop(self._container)

    def __repr__(self) -> str:
        return repr(self._container)

def astar(inital:T,goal_test:Callable[[T],bool],successors:Callable[[T],List[T]],heurisitc:Callable[[T],float]) -> Optional[Node[T]]:
    frontier: PriorityQueue[Node[T]] = PriorityQueue()
    frontier.push(Node(inital,None,0.0,heurisitc(inital)))
    explored: Dict[T,float] ={inital:0.0}
    while not frontier.empty:
        current_node:Node[T] = frontier.pop()
        current_state: T = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            new_cost: float = current_node.cost + 1
            if child not in explored or explored[child] > new_cost:
                explored[child] = new_cost
                frontier.push(Node(child,current_node,new_cost,heurisitc(child)))
    return None

def node_to_path(node:None[T]) -> List[T]:
    path: List[T] = [node.state]
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path


C = TypeVar("C",bound="Comparable")
class Comparable(Protocol):
    def __gt__(self: C, other:C) -> bool:
        return (not self < other) and self != other

    def __le__(self:C, other:C) -> bool:
        print("sourt:{}".format(C))
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
    return False


if __name__ == "__main__":
    print(linear_contains([1,5,15,15,15,20],5))
    print(binary_contains(["a","d","e","f","z"],"f"))
    print(binary_contains(["john","mark","ronald","sarah","abby"],"abby"))


