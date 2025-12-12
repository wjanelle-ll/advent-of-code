from typing import TypedDict
import typing

input = open('input.txt').read()

class Node(TypedDict):
    id: str
    children_ids: list[str]
    out_paths: typing.Optional[int]
    dac_paths: typing.Optional[int]
    fft_paths: typing.Optional[int]
    both_paths: typing.Optional[int]

nodes: dict[str, Node] = {}

for line in input.splitlines():
    nodes[line.split(":")[0]] = {
        "id": line.split(":")[0],
        "children_ids": [
            child
            for child in line.split(":")[1].split()
        ],
        "out_paths": None,
        "dac_paths": None,
        "fft_paths": None,
        "both_paths": None,
    }

def search_node(node: Node, found_dac: bool, found_fft: bool) -> typing.Tuple[int, int, int, int]:
    # try cache
    if node["out_paths"] is None:
        node["out_paths"] = 0
        node["dac_paths"] = 0
        node["fft_paths"] = 0
        node["both_paths"] = 0

        # search
        for child_id in node["children_ids"]:
            if child_id == "out":
                node["out_paths"] += 1
            else:
                results = search_node(nodes[child_id], found_dac, found_fft)
                node["out_paths"] += results[0]
                node["dac_paths"] += results[1]
                node["fft_paths"] += results[2]
                node["both_paths"] += results[3]
                if child_id == "dac":
                    node["dac_paths"] += results[0]
                    node["both_paths"] += results[2]
                if child_id == "fft":
                    node["fft_paths"] += results[0]
                    node["both_paths"] += results[1]

    return (node["out_paths"], node["dac_paths"], node["fft_paths"], node["both_paths"])

print(search_node(nodes["svr"], False, False)[3])
