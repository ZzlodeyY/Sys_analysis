import json
import typing as tp

TEST_STRING = """
    {
        "1": {
            "2": {
                "3": {
                    "5": {},
                    "6": {}
                },
                "4": {
                    "7": {},
                    "8": {}
                }
            }
        }
    }
"""

def get_object_from_json_string(object_string: str) -> tp.Dict[str, tp.Any]:
    return json.loads(object_string)

def create_node(children: tp.List[int], parent: tp.Optional[str]) -> tp.Dict:
    return {
        "children": children,
        "parent": parent,
        "relations": [0] * 5
    }

def recursive_graph_parse(
    graph: tp.Dict[str, tp.Dict],
    graph_repr: tp.Dict[str, tp.Dict],
    parent: tp.Optional[str]=None
) -> None:
    for key, val in graph.items():
        children = []
        if isinstance(val, dict) and val != dict():
            recursive_graph_parse(val, graph_repr, key)
            children = list(val.keys())
            
        graph_repr[key] = create_node(children, parent)
        graph_repr[key]["relations"][0] = len(children)
        graph_repr[key]["relations"][1] = 1 if parent is not None else 0

def relations_parse(graph_repr: tp.Dict[str, tp.Dict]) -> None:
    for key, val in graph_repr.items():
        if val["parent"] is not None:
            parent = val["parent"]
            graph_repr[key]["relations"][4] += len(graph_repr[parent]["children"]) - 1
            if graph_repr[parent]["parent"] is not None:
                graph_repr[key]["relations"][3] += 1
                
        for child in val["children"]:
            graph_child = graph_repr[str(child)]
            graph_repr[key]["relations"][2] += graph_child["relations"][2] + len(graph_child["children"])
            graph_child["relations"][3] += graph_repr[key]["relations"][3]

def main(input_string: str) -> None:
    source_graph = get_object_from_json_string(input_string)
    graph_repr = {}
    recursive_graph_parse(source_graph, graph_repr)
    relations_parse(graph_repr)
    sorted_repr = {key: val for key, val in sorted(graph_repr.items(), key=lambda x: x[0])}
    
    for key, value in sorted_repr.items():
        print(f"{key}: {value['relations']}")

if __name__ == "__main__":
    main(TEST_STRING)