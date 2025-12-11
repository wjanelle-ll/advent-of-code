from typing import TypedDict
import typing

input = open('input.txt').read()

class Node(TypedDict):
    children_ids: list[str]
    known_out_path_count: typing.Optional[int]

nodes: dict[str, Node] = {}

for line in input.splitlines():
    nodes[line.split(":")[0]] = {
        "children_ids": [
            child
            for child in line.split(":")[1].split()
        ],
        "known_out_path_count": None,
    }

def search_node(node: Node):
    # try cache
    if node["known_out_path_count"] is not None:
        return node["known_out_path_count"]
    node["known_out_path_count"] = 0

    # search
    out_paths = 0
    for child_id in node["children_ids"]:
        if child_id == "out":
            out_paths += 1
        else:
            out_paths += search_node(nodes[child_id])
    
    node["known_out_path_count"] = out_paths
    return out_paths

print(search_node(nodes["you"]))
