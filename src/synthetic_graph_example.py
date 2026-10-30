"""نمونه آموزشی ساخت گراف مصنوعی کوچک؛ داده واقعی شیراز نیست."""
import networkx as nx

def build_synthetic_graph():
    graph = nx.DiGraph()
    # گره‌ها فقط شناسه‌های آزمایشی هستند.
    graph.add_weighted_edges_from([
        ("A", "B", 100), ("B", "D", 100),
        ("A", "C", 130), ("C", "D", 80),
        ("B", "C", 60),
    ], weight="length")
    return graph

if __name__ == "__main__":
    G = build_synthetic_graph()
    print("Synthetic nodes:", G.number_of_nodes())
    print("Synthetic edges:", G.number_of_edges())
    print("Example shortest distance A->D:",
          nx.shortest_path_length(G, "A", "D", weight="length"))
