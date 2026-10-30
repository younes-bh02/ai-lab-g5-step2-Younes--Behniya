"""نمونه مفهومی اعمال بسته‌شدن روی کپی گراف؛ گراف اصلی حفظ می‌شود."""
import copy
import networkx as nx

def apply_closure(graph, edge_u, edge_v):
    """یک کپی از گراف می‌سازد و یال جهت‌دار مشخص را در آن می‌بندد."""
    scenario_graph = copy.deepcopy(graph)
    if scenario_graph.has_edge(edge_u, edge_v):
        scenario_graph.remove_edge(edge_u, edge_v)
    return scenario_graph

if __name__ == "__main__":
    base = nx.DiGraph()
    base.add_weighted_edges_from(
        [("A", "B", 1), ("B", "D", 1), ("A", "C", 2), ("C", "D", 2)],
        weight="length"
    )
    changed = apply_closure(base, "A", "B")
    print("Base graph still has A->B:", base.has_edge("A", "B"))
    print("Scenario graph has A->B:", changed.has_edge("A", "B"))
    print("Alternative route:", nx.shortest_path(changed, "A", "D", weight="length"))
