from __future__ import annotations
from enum import Enum
from typing import List,NamedTuple,Callable,Optional
import random
from search.generic_search import Node,dfs,node_to_path,bfs,astar
from math import sqrt

class Cell(str,Enum):
    EMPTY = "E"
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    row: int
    column: int

class Maze:
    def __init__(self, rows: int = 10, coloumns: int = 10,sparsenenss: float = 0.2, start: MazeLocation = MazeLocation(0,0), goal: MazeLocation = MazeLocation(9,9)) -> None:
        self._rows: int = rows
        self._cloumns: int = coloumns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(coloumns)] for r in range(rows)]
        self._randomly_fill(rows,coloumns,sparsenenss)
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self,rows: int ,columns: int,sparseness:float):
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0,1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def goal_test(self,m1: MazeLocation) -> bool:
        return m1 == self.goal

    def successors(self,m1:MazeLocation) -> List[MazeLocation]:
        locations: List[MazeLocation] = []
        if m1.row + 1 < self._rows and self._grid[m1.row + 1][m1.column] != Cell.BLOCKED:
            locations.append(MazeLocation(m1.row+1,m1.column))
        if m1.row - 1 >= 0 and self._grid[m1.row - 1][m1.column] != Cell.BLOCKED:
            locations.append(MazeLocation(m1.row-1,m1.column))
        if m1.column + 1 < self._cloumns and self._grid[m1.row][m1.column +1] != Cell.BLOCKED:
            locations.append(MazeLocation(m1.row, m1.column+1))
        if m1.column - 1 > 0 and self._grid[m1.row][m1.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(m1.row, m1.column - 1))
        return locations

    def mark(self,path:List[MazeLocation]):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "".join([c.value for c in row]) + "\n"
        return output

def euclidean_distance(goal:MazeLocation) -> Callable[[MazeLocation],float]:
    def distance(m1:MazeLocation) -> float:
        xdist: int = m1.column - goal.column
        ydist: int = m1.row - goal.row
        return sqrt((xdist*xdist)+(ydist*ydist))
    return distance


if __name__ == "__main__":
    maze: Maze = Maze()
    print(maze)
    #solution1:Optional[Node[MazeLocation]] = dfs(maze.start,maze.goal_test,maze.successors)
    #solution1: Optional[Node[MazeLocation]] = bfs(maze.start, maze.goal_test, maze.successors)
    distance: Callable[[MazeLocation],float] = euclidean_distance(maze.goal)
    solution1: Optional[Node[MazeLocation]] = astar(maze.start, maze.goal_test, maze.successors,distance)
    if solution1 is None:
        print("no soluation found")
    else:
        print("found")
        path1:List[MazeLocation] = node_to_path(solution1)
        maze.mark(path1)
        print(maze)



