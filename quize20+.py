def skyline(**kwargs):
    # returns the tallest building key and value
    #tallest_building = max(kwargs, key=kwargs.get)
    #return tallest_building, kwargs[tallest_building]
    tellest_building = ()
    for building, height in kwargs.items():
        if not tellest_building or height > tellest_building[1]:
            tellest_building = (building, height)
    return tellest_building

    


def get_skyline():
    skyline_input = input()
    return {str(k): int(v) for k, v in (pair.split(':') for pair in skyline_input.split())}

skyline_data = get_skyline()
#print(skyline_data)
tallest_skyline = skyline(**skyline_data)
print(tallest_skyline)
print(f"The tallest building is {tallest_skyline[0]} with a height of {tallest_skyline[1]}.")

