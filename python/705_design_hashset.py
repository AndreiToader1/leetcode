class MyHashSet:

    def __init__(self):
        MAX_VALUE = 10**6+1
        self.__hash_set = [False] * MAX_VALUE
    def add(self, key: int) -> None:
        self.__hash_set[key] = True

    def remove(self, key: int) -> None:
        self.__hash_set[key] = False

    def contains(self, key: int) -> bool:
        return self.__hash_set[key] == True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    hash_set = MyHashSet()
    hash_set.add(1)
    hash_set.add(2)
    print(hash_set.contains(1))
    print(hash_set.contains(3))
    hash_set.add(2)
    print(hash_set.contains(2))
    hash_set.remove(2)
    print(hash_set.contains(3))
