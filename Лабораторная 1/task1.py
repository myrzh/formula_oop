import doctest


class Table:
    """
    Класс, описывающий стол.
    Атрибуты:
        material (str): Материал стола.
        height (float): Высота стола в сантиметрах.
        width (float): Ширина стола в сантиметрах.
    """

    def __init__(self, material: str, height: float, width: float):
        self.material = material
        self.height = height
        self.width = width

    def fold(self) -> None:
        """
        Складывает стол.
        """
        ...

    def move(self, new_location: str) -> None:
        """
        Перемещает стол в новое место.

        Args:
            new_location (str): Новое местоположение стола.

        >>> table = Table("wood", 75.0, 120.0)
        >>> table.move("living room")
        """
        ...


class Tree:
    """
    Класс, описывающий дерево.
    Атрибуты:
        species (str): Вид дерева.
        age (int): Возраст дерева в годах.
        height (float): Высота дерева в метрах.
    """

    def __init__(self, species: str, age: int, height: float):
        self.species = species
        self.age = age
        self.height = height

    def grow(self, years: int) -> None:
        """
        Увеличивает возраст дерева на заданное количество лет.

        Args:
            years (int): Количество лет для роста.

        >>> tree = Tree("oak", 10, 5.0)
        >>> tree.grow(5)
        """
        ...

    def shed_leaves(self) -> None:
        """
        Дерево сбрасывает листья.
        """
        ...


class Stack:
    """
    Класс, описывающий стек.
    Атрибуты:
        items (list): Элементы стека.
    """

    def __init__(self):
        self.items = []

    def push(self, item: int) -> None:
        """
        Добавляет элемент в стек.

        Args:
            item (int): Элемент для добавления.

        >>> stack = Stack()
        >>> stack.push(1)
        """
        ...

    def pop(self) -> int:
        """
        Удаляет и возвращает верхний элемент стека.

        Returns:
            int: Верхний элемент стека.

        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.pop()
        1
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
