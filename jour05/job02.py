def draw_rectangle(width, height):
    for i in range(height):
        for j in range(width):
            if i == 0 or i == height - 1:
                print("-" if j > 0 and j < width - 1 else "|", end="")
            else:
                print(" " if j > 0 and j < width - 1 else "|", end="")
        print()
draw_rectangle(5, 5)
draw_rectangle(15, 6)
