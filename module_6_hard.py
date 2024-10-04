from math import pi, sqrt


class Figure:
    sides_count = 0

    def set_sides(self, *args):
        new_sides = [*args]
        if self.__is_valid_sides(new_sides) is True:
            self.__sides = new_sides

    def __is_valid_sides(self, my_list):
        if len(my_list) == self.sides_count:
            for i in my_list:
                if i < 0:
                    return False
            return True
        else:
            return False

    def __init__(self, color, sides, filled=bool):

        self.__color = list(color)
        self.__sides = [sides for i in range(self.sides_count)]
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self, R, G, B):

        if 0 < R <= 255 and 0 < G <= 255 and 0 < B <= 255:
            return True
        else:
            return False

    def set_color(self, R, G, B):
        if self.__is_valid_color(R, G, B) is True:
            self.__color = [R, G, B]

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__sides = sides
        self.__radius = self.__sides[0] / (2 * pi)

    def get_square(self):
        s = (self.__radius ** 2) * pi
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__sides = sides

    def get_volume(self):
        return self.__sides ** 3


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.sides = sides
        p = (self.sides[0] + self.sides[1] + self.sides[2]) / 2
        self.__height = 2 * (sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))) / self.sides[0]

    def get_square(self):
        St = (self.__height * self.sides[0]) / 2
        return St


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
