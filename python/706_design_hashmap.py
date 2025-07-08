class MyHashMap:

    def __init__(self):
        MAX_NUMBER = 10**6 +1
        self.DEFAULT_HASHMAP_VALUE = -1
        self.__hash_map = [-1] * MAX_NUMBER
    def put(self, key: int, value: int) -> None:
        self.__hash_map[key] = value

    def get(self, key: int) -> int:
        return self.__hash_map[key]

    def remove(self, key: int) -> None:
        self.__hash_map[key] = self.DEFAULT_HASHMAP_VALUE


if __name__ == '__main__':
    hash_map = MyHashMap()
    hash_map.put(1,1)
    hash_map.put(2,2)
    print(hash_map.get(1))
    print(hash_map.get(3))
    hash_map.put(2,1)
    print(hash_map.get(2))
    hash_map.remove(2)
    print(hash_map.get(2))
