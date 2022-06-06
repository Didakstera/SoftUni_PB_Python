from math import pi

figure_type = input()
if figure_type == "square":
     square_side = float(input())
     area_square = square_side * square_side
     print(area_square)
if figure_type == "rectangle":
     rectangle_side_a = float(input())
     rectangle_side_b = float(input())
     area_rectangle = rectangle_side_a * rectangle_side_b
     print(area_rectangle)
if figure_type == "circle":
    circle_radius = float(input())
    area_circle = circle_radius * circle_radius * pi
    print(area_circle)
if figure_type == "triangle":
    triangle_side = float(input())
    triangle_height_to_side = float(input())
    area_triangle = triangle_side * triangle_height_to_side / 2
    print(area_triangle)
