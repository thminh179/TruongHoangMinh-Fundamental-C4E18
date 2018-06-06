map_sokoban ={
    'size_x': 5,
    'size_y': 5
}

player = {
    "x": 4,
    "y": 0
}

boxes = [
    {'x': 1, 'y': 1},
    {'x': 2, 'y': 2},
    {'x': 3, 'y': 3}
]

for y in range (map_sokoban['size_y']):
    
    box_is_here = False
    
    for x in range (map_sokoban['size_x']):
        for box in boxes:
            if box['x'] == x and box['y'] == y:
                print("B ", end="")
                box_is_here =True

        if x == player['x'] and y == player['y']:
            print("P ", end="")
        elif box_is_here is not True: 
            print("- ", end="")

    print()