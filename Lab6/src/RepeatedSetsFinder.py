from collections import Counter

class RepeatedSetFinder:
    def __init__(self, numbers: list[int]):
        self.numbers = numbers

    def find_repeated_sets(self,size: int) -> list[int]:
        count = Counter(self.numbers)
        return [num for num, freq in count.items() if freq == size]

