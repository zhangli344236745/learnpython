from __future__ import annotations
from typing import TypeVar,Generic,List,Optional
from dataclasses import dataclass
import sys
sys.path.insert(0,"..")
from search.generic_search import bfs,Node,node_to_path

@dataclass
class Edge:
    u: int
    v: int

    def reversed(self) -> Edge:
        return Edge(self.v,self.u)

    def __str__(self) -> str:
        return f"{self.u} -> {self.v}"

V = TypeVar("V")

class Graph(Generic[V]):
    def __init__(self,vertices:List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges:List[List[Edge]] = [[] for _ in vertices]

    @property
    def vertex_count(self) -> int:
        return len(self._vertices)

    @property
    def edge_count(self) -> int:
        return sum(map(len,self._edges))

    def add_vertex(self,vertex:V) -> int:
        self._vertices.append(vertex)
        self._edges.append([])
        return self.vertex_count - 1

    def add_edge(self,edge:Edge) -> None:
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self,u:int,v:int) -> None:
        edge:Edge = Edge(u,v)
        self.add_edge(edge)

    def add_edge_by_vertices(self,first:V,second:V) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u,v)

    def vertex_at(self,index:int) -> V:
        return self._vertices[index]

    def index_of(self,vertex:V) -> int:
        return self._vertices.index(vertex)

    def neighbors_for_index(self,index:int) -> List[V]:
        return list(map(self.vertex_at,[e.v for e in self._edges[index]]))

    def neighbors_for_vertex(self,vertex:V) -> List[V]:
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self,index:int) -> List[Edge]:
        return self._edges[index]


    def __str__(self) -> str:
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f" {self.vertex_at(i)} -> {self.neighbors_for_index(i)} \n"
        return desc

if __name__ == "__main__":
    city_graph:Graph[str] = Graph(["Seattle","San Francisco","Los Angeles","Riverside","Phoenix","Chicago",
                                   "Boston","New York","Atlanta","Miami",
                                   "Dallas","Houston","Detroit","Philadelphia","Washington"])
    city_graph.add_edge_by_vertices("Seattle","Chicago")
    city_graph.add_edge_by_vertices("Seattle","San Francisco")
    city_graph.add_edge_by_vertices("San Francisco","Riverside")
    city_graph.add_edge_by_vertices("San Francisco","Los Angeles")
    city_graph.add_edge_by_vertices("Los Angeles","Riverside")
    city_graph.add_edge_by_vertices("Los Angeles","Phoenix")
    print(city_graph)
    bfs_result:Optional[Node[V]] = bfs("Boston",lambda x : x == "Miami",city_graph.neighbors_for_vertex)
    if bfs_result is None:
        print("no solution found")
    else:
        path:List[V] = node_to_path(bfs_result)
        print("path from boston to miami")
        print(path)

