origin_coordinates = (0, 0)
a_coordinates = (3, 4)
x1, y1 = origin_coordinates
x2, y2 = a_coordinates
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f"{distance:.2f}")