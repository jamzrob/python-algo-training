import os
from pathlib import Path
from katas.dsa import dsa, dsa_list
import shutil

katas_path = Path.cwd() / "katas"
dir_list = list(filter(lambda d: d.startswith("day"), os.listdir(katas_path)))
day_num = max(map(lambda d: int(d[-1]), dir_list)) + 1

day_path = katas_path / f"day{str(day_num)}"
os.mkdir(day_path)

def generate_method(method):
    return f"    def {method['name']}(self, {method.get('args', '')}):\n\
        pass\n"


def generate_property(prop):
    return f"{prop['name']}: {prop['type']}"

def generate_property_set(prop):
    return f"        self.{prop['name']}= {prop['name']}\n"


def generate_getter(getter):
    return f"    @property\n    def {getter['name']}(self):\
    return self._{getter['prop_name']}\n"


def create_class(name, item):
    class_content = f"class {name}{item.get("generic")}: \n\n    def __init__(self, "
    class_content += ",".join(
        [generate_property(prop) for prop in item.get("properties", [])]
    )
    class_content += "):\n"
    class_content += "\n".join(
        [generate_property_set(prop) for prop in item.get("properties", [])]
    )
    class_content += "\n"
    class_content += "\n".join(
        [generate_getter(getter) for getter in item.get("getters", [])]
    )
    class_content += "\n".join(
        [generate_method(method) for method in item.get("methods", [])]
    )
    with open(Path(day_path, f"{name}.py"), "w") as file:
        file.write(class_content)


def create_function(name, item):
    function_content = f"def {item['fn']}({item.get('args', '')}):\n\
    pass\n"
    with open(Path(day_path, f"{name}.py"), "w") as file:
        file.write(function_content)


if __name__ == "__main__":
    for ds in dsa_list:
        if ds not in dsa:
            raise RuntimeError(f"{ds} not found in dsa")
        item = dsa[ds]
        with open(Path(day_path, f"__init__.py"), "w") as file:
            file.write("from .BinarySearchList import bs_list \n\
from .BubbleSort import bubble_sort \n\
from .DoublyLinkedList import DoublyLinkedList \n\
from .LRU import LRU \n\
from .MazeSolver import solve \n\
from .MinHeap import MinHeap \n\
from .Queue import Queue \n\
from .QuickSort import quick_sort \n\
from .SinglyLinkedList import SinglyLinkedList \n\
from .Stack import Stack \n\
from .Trie import Trie \n\
from .TwoCrystalBalls import two_crystal_balls \n\
from .MergeSort import merge_sort \n\
")
        if item["type"] == "class":
            create_class(ds, item)
        else:
            create_function(ds, item)
