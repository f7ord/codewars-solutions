def tower_builder(n_floors):
    floors = [1]
    floor_count = 1
    while floor_count != n_floors:
        floors.append(floors[-1]+2)
        floor_count += 1
    return [('*'*floor).center(max(floors)) for floor in floors]


def tower_builder(n_floors):
    return [('*' * ((i*2)-1)).center((n_floors*2)-1) for i in range(1, n_floors+1)]
