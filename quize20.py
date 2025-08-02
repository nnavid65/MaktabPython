def skyline(*args):
    heights = 0
    [heights := height for height in args if height > heights]
    return heights

def get_heights():
    heights = input()
    return [int(height) for height in heights.split()]

buildings_heights = get_heights()
highest_buildings = skyline(*buildings_heights)
print(highest_buildings)
