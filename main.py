from canvas import Canvas
from shapes import Square, Rectangle

canvas_width = int(input("Enter the canvas width: "))
canvas_height = int(input("Enter the canvas height: "))

colors = {"white": (255, 255, 255), "black": (0, 0, 0)}
canvas_color = input("Enter the canvas color (black or white): ")

canvas1 = Canvas(canvas_width, canvas_height, colors[canvas_color])


while True:
    shape_type = input("What do you want to draw? Enter quit to quit. ")
    # ask for rectangle data and create rectangle if user enters rectangle
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of starting point of rectangle: "))
        rec_y = int(input("Enter y of starting point of rectangle: "))
        rec_width = int(input("Enter width of rectangle: "))
        rec_height = int(input("Enter height of rectangle: "))
        red = int(input("How much red should the rectangle have: "))
        green = int(input("How much green should the rectangle have: "))
        blue = int(input("How much blue should the rectangle have: "))

        r1 = Rectangle(rec_x, rec_y, rec_width, rec_height, (red, green, blue))
        r1.draw(canvas1)

    if shape_type.lower() == "square":
        # ask for square data and create square if user entered square
        sqr_x = int(input("Enter x of starting point of square: "))
        sqr_y = int(input("Enter y of starting point of square: "))
        sqr_side = int(input("Enter side length of square: "))
        red = int(input("How much red should the square have: "))
        green = int(input("How much green should the square have: "))
        blue = int(input("How much blue should the square have: "))

        s1 = Square(sqr_x, sqr_y, sqr_side, (red, green, blue))
        s1.draw(canvas1)

    if shape_type.lower() == "quit":
        break

canvas1.make("Hello.png")
