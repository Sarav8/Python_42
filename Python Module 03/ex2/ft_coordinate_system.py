import sys
import math

def ft_coordinate_system():
    print("=== Game Coordinate System ===")
    coord1 = (10 , 20, 5)
    distance1 = (0, 0, 0)
    x0, y0, z0 = coord1
    x1, y1, z1 = distance1
    result1= math.sqrt((x0-x1)**2 + (y0-y1)**2 + (z0-z1)**2)
    print(f"Position created: {coord1}")
    print(f"Distance between {distance1} and {coord1}: {result1:.2f}\n")

    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}" ')
    coord_split = coord_str.split(',')
    i = 0
    coord_list = []
    while i < 3:
            coord_parse= int(coord_split[i])
            coord_list.append(coord_parse)
            i += 1
    print(f"Parsed position: {tuple(coord_list)}")
    x2, y2, z2 = coord_list
    result2 = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    print(f"Distance between {distance1} and {coord_list}: {result2:.2f}\n")

    print('Parsing invalid coordinates: "abc,def,ghi"')
    coord_invalid = "abc,def,ghi"
    coord_invalid_split = coord_invalid.split(',')
    coord_list_str = []
    i = 0
    while i < 3:
        try:
            coord_list_str.append(int(coord_invalid_split[i]))
            i += 1
        except ValueError as e:
            print(f"Error parsing coordinates: {e}")
            print(f"Error details - Type: {type(e).__name__}, Args: {e}\n")
            break
    
    print("Unpacking demonstration:")
    print(f"Player at x= {x2}, y={y2}, z={z2}")
    print(f"Coordinates: X={x2}, Y={y2}, Z={z2}")



if __name__ == "__main__":
    ft_coordinate_system()