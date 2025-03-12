class IterableWithGenerator:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return (item for item in self.data)  # Генераторное выражение

# Пример использования:
iterable = IterableWithGenerator([1, 2, 3, 4, 5])

for num in iterable:
    print(num)