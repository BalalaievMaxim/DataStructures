from typing import Any
from linked_list import LinkedList


class HashTable:
    def __init__(self, size: int) -> None:
        self.size = size
        self.entries = [LinkedList() for _ in range(size)]

    def add(self, key, value) -> None:
        if not key in self.keys():
            index = hash(key) % self.size
            bucket = self.entries[index]
            bucket.add_last((key, value))
        else:
            raise KeyError(f"{key} already exists")

    def get(self, key) -> Any | None:
        index = hash(key) % self.size
        bucket = self.entries[index]

        result = bucket.find(lambda x: x[0] == key)
        return result[1] if result else None
    
    def __iter__(self):
        for bucket in self.entries:
            for node in bucket:
                yield node
                
    def clear(self) -> None:
        for bucket in self.entries:
            bucket.clear()
            
    def keys(self) -> list:
        return [node.value[0] for node in self]
    
    def values(self) -> list:
        return [node.value[1] for node in self]
    
    def entities(self) -> list:
        return [node.value for node in self]
    
    def clone(self) -> "HashTable":
        new = HashTable(self.size)
        for key, value in self.entities():
            new.add(key, value)
        return new


if __name__ == "__main__":
    ht = HashTable(size=50)
    ht.add(1, "val")
    ht.add(51, "fsdgd")
    ht.add(2, "val2")
    ht.add("jonh", "val3")
    print(ht.get("jonh"))
