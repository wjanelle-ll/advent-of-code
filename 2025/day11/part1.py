from typing import TypedDict

input = open('input.txt').read()

class Node(TypedDict):
    id: str
    children_ids: list[str]

nodes: list[Node] = []

for line in input.splitlines():
    nodes.append({
        "id": line.split(":")[0],
        "children_ids": [
            child
            for child in line.split(":")[1].split()
        ]
    })

def find_node(id: str):
    for node in nodes:
        if node["id"] == id:
            return node

out_paths = 0
def search_node(node: Node):
    global out_paths
    for child_id in node["children_ids"]:
        if child_id == "out":
            out_paths += 1
        else:
            search_node(find_node(child_id))

search_node(find_node("you"))
print(out_paths)
