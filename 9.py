class Rectangle:
    """
    A class to represent a rectangle with width and length.

    :param width: The width of the rectangle.
    :type width: int or float
    :param length: The length of the rectangle.
    :type length: int or float
    """

    def __init__(self, width, length):
        """
        Initialize the Rectangle with width and length.

        :param width: The width of the rectangle.
        :type width: int or float
        :param length: The length of the rectangle.
        :type length: int or float
        """
        self.width = width
        self.length = length

    def calculate_area(self):
        """
        Calculate the area of the rectangle.

        :return: The area of the rectangle (width * length).
        :rtype: int or float
        """
        return self.width * self.length

    def calculate_perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        :return: The perimeter of the rectangle (2 * (width + length)).
        :rtype: int or float
        """
        return 2 * (self.width + self.length)


# Test of the Rectangle class
rectangle = Rectangle(5, 3)  # 5: width & 3: length
print("Largeur:", rectangle.width)
print("Longueur:", rectangle.length)
print("Aire:", rectangle.calculate_area())
print("Périmètre:", rectangle.calculate_perimeter())
