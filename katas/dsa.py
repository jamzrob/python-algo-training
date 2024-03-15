length_property = {
    "properties": [
        {
            "name": "length",
            "type": "int",
            "scope": "public",
        }
    ]
}

list_interface = {
    "methods": [
        {
            "name": "prepend",
            "args": "item: T",
            "ret": "void",
        },
        {
            "name": "insertAt",
            "args": "item: T, idx: int",
            "ret": "void",
        },
        {
            "name": "append",
            "args": "item: T",
            "ret": "void",
        },
        {
            "name": "remove",
            "args": "item: T",
            "ret": "T | None",
        },
        {
            "name": "get",
            "args": "idx: int",
            "ret": "T | None",
        },
        {
            "name": "removeAt",
            "args": "idx: int",
            "ret": "T | None",
        },
    ],
    "properties": length_property["properties"],
}

dsa_list = [
    "DFSOnBST",
    "LRU",
    "LinearSearchList",
    "BinarySearchList",
    "TwoCrystalBalls",
    "BubbleSort",
    "SinglyLinkedList",
    "DoublyLinkedList",
    "Queue",
    "Stack",
    "ArrayList",
    "MazeSolver",
    "QuickSort",
    "BTPreOrder",
    "BTInOrder",
    "BTPostOrder",
    "BTBFS",
    "CompareBinaryTrees",
    "DFSOnBST",
    "DFSGraphList",
    "Trie",
    "BFSGraphMatrix",
    "Map",
    "MinHeap",
]

dsa = {
    "LRU": {
        "type": "class",
        "methods": [
            {
                "name": "update",
                "args": "key: int, value: string",
                "ret": "void",
            },
            {
                "name": "get",
                "args": "key: int",
                "ret": "V | None",
            },
        ],
        "properties": [
            {
                "name": "length",
                "type": "int",
                "scope": "private",
            }
        ],
    },
    "MinHeap": {
        "type": "class",
        "methods": [
            {
                "name": "insert",
                "args": "value: int",
                "ret": "void",
            },
            {
                "name": "delete",
                "args": "",
                "ret": "int",
            },
        ],
        "properties": [
            {
                "name": "length",
                "type": "int",
                "scope": "public",
            }
        ],
    },
    "Map": {
        "generic": "Mapping[T, V]",
        "type": "class",
        "methods": [
            {
                "name": "get",
                "args": "key: T",
                "ret": "V | None",
            },
            {
                "name": "set",
                "args": "key: T, value: V",
                "ret": "void",
            },
            {
                "name": "delete",
                "args": "key: T",
                "ret": "V | None",
            },
            {
                "name": "size",
                "ret": "int",
            },
        ],
    },
    "RingBuffer": {
        "generic": "[T]",
        "type": "class",
        "methods": [
            {
                "name": "push",
                "args": "item: T",
                "ret": "void",
            },
            {
                "name": "get",
                "args": "idx: int",
                "ret": "T | None",
            },
            {
                "name": "pop",
                "ret": "T | None",
            },
        ],
        "properties": [
            {
                "name": "length",
                "type": "int",
                "scope": "public",
            }
        ],
    },
    "ArrayList": {
        "type": "class",
        "generic": "[T]",
        "methods": list_interface["methods"],
        "properties": list_interface["properties"],
    },
    "SinglyLinkedList": {
        "generic": "[T]",
        "type": "class",
        "methods": list_interface["methods"],
        "properties": list_interface["properties"],
    },
    "DoublyLinkedList": {
        "generic": "[T]",
        "type": "class",
        "methods": list_interface["methods"],
        "properties": list_interface["properties"],
    },
    "Queue": {
        "generic": "[T]",
        "type": "class",
        "properties": length_property["properties"],
        "methods": [
            {
                "name": "enqueue",
                "args": "item: T",
                "ret": "void",
            },
            {
                "name": "deque",
                "args": "",
                "ret": "T | None",
            },
            {
                "name": "peek",
                "args": "",
                "ret": "T | None",
            },
        ],
    },
    "Stack": {
        "generic": "[T]",
        "type": "class",
        "properties": length_property["properties"],
        "methods": [
            {
                "name": "push",
                "args": "item: T",
                "ret": "void",
            },
            {
                "name": "pop",
                "args": "",
                "ret": "T | None",
            },
            {
                "name": "peek",
                "args": "",
                "ret": "T | None",
            },
        ],
    },
    "Trie": {
        "type": "class",
        "properties": length_property["properties"],
        "methods": [
            {
                "name": "insert",
                "args": "item: str",
                "ret": "void",
            },
            {
                "name": "delete",
                "args": "item: str",
                "ret": "void",
            },
            {
                "name": "find",
                "args": "partial: str",
                "ret": "list[int]",
            },
        ],
    },
    "BubbleSort": {
        "type": "fn",
        "fn": "bubble_sort",
        "args": "arr: list[int]",
        "ret" "": "void",
    },
    "InsertionSort": {
        "type": "fn",
        "fn": "insertion_sort",
        "args": "arr: list[int]",
        "ret" "": "void",
    },
    "MergeSort": {
        "type": "fn",
        "fn": "merge_sort",
        "args": "arr: list[int]",
        "ret" "": "void",
    },
    "QuickSort": {
        "type": "fn",
        "fn": "quick_sort",
        "args": "arr: list[int]",
        "ret" "": "void",
    },
    "DijkstraList": {
        "type": "fn",
        "fn": "dijkstra_list",
        "args": "source: int, sink: int, arr: list[list[int]]",
        "ret" "": "list[int]",
    },
    "PrimsList": {
        "type": "fn",
        "fn": "prims",
        "args": "list: list[list[int]]",
        "ret": "list[int] | None",
    },
    "BinarySearchList": {
        "type": "fn",
        "fn": "bs_list",
        "args": "haystack: list[int], needle: int",
        "ret": "boolean",
    },
    "LinearSearchList": {
        "type": "fn",
        "fn": "linear_search",
        "args": "haystack: list[int], needle: int",
        "ret": "boolean",
    },
    "TwoCrystalBalls": {
        "type": "fn",
        "fn": "two_crystal_balls",
        "args": "breaks: boolean[]",
        "ret": "int",
    },
    "MazeSolver": {
        "type": "fn",
        "fn": "solve",
        "args": "maze: str[], wall: str, start: Point, end: Point",
        "ret": "str[]",
    },
    "BTPreOrder": {
        "type": "fn",
        "fn": "pre_order_search",
        "args": "head: BinaryNode[int]",
        "ret": "np.ndarray",
    },
    "BTInOrder": {
        "type": "fn",
        "fn": "in_order_search",
        "args": "head: BinaryNode[int]",
        "ret": "np.ndarray",
    },
    "BTPostOrder": {
        "type": "fn",
        "fn": "post_order_search",
        "args": "head: BinaryNode[int]",
        "ret": "np.ndarray",
    },
    "BTBFS": {
        "type": "fn",
        "fn": "bfs",
        "args": "head: BinaryNode[int], needle: int",
        "ret": "boolean",
    },
    "CompareBinaryTrees": {
        "type": "fn",
        "fn": "compare",
        "args": "a: BinaryNode[int] | None, b: BinaryNode[int] | None",
        "ret": "boolean",
    },
    "DFSOnBST": {
        "type": "fn",
        "fn": "dfs",
        "args": "head: BinaryNode[int], needle: int",
        "ret": "boolean",
    },
    "DFSGraphList": {
        "type": "fn",
        "fn": "dfs",
        "args": "graph: list[list[int]], source: int, needle: int",
        "ret": "None",
    },
    "BFSGraphList": {
        "type": "fn",
        "fn": "bfs",
        "args": "graph: list[list[int]], source: int, needle: int",
        "ret": "None",
    },
    "BFSGraphMatrix": {
        "type": "fn",
        "fn": "bfs",
        "args": "graph: list[list[int]], source: int, needle: int",
        "ret": "None",
    },
}
