from __future__ import annotations
from typing import TypeVar,Generic,List,Tuple
import sys
sys.path.insert(0,'..')
from graph.weighted_edge import WeightedEdge
from graph.graph import Graph

V = TypeVar("V")

class WeightedGraph(Generic[V],Graph[V]):
    def __init__(self,vertices:List[V] = []) -> None:
        self._vertices: List[V] = vertices
        self._edges: List[List[WeightedEdge]] - [[] for _ in vertices]

    def add_edge_by_indices(self,u:int,v:int,weight:float) -> None:
        edge: WeightedEdge = WeightedEdge(u,v,weight)
        self.add_edge(edge)

    def add_edge_by_vertices(self,first:V,sencod:V,weight:float) -> None:
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(sencod)
        self.add_edge_by_indices(u,v,weight)

    def neighbors_for_index_with_weight(self,index:int) -> List[Tuple[V,float]]:
        distance_tuples: List[Tuple[V,float]] = []
        for edge in self.edges_for_index(index):
            distance_tuples.append((self.vertex_at(edge.v),edge.weight))
        return distance_tuples

    def __str__(self) -> str:
        desc:str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index_with_weight(i)} \n"
        return desc