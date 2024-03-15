# ****************************************************************************************************
#
#       This program will draw a pentagon using the canvas widget class and display my name in
#       yellow text in the center of the pentagon.
#
# ****************************************************************************************************

import tkinter as tk
import tkinter.font as tkfont

# ****************************************************************************************************


class Polygon:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Polygon")

        self.canvas = tk.Canvas(self.main_window, width=300, height=300)

        # hexagon vertices - 6 sides
        # self.vertices = [200, 50, 250, 150, 200, 250, 100, 250, 50, 150, 100, 50]

        # octagon vertices - 8 sides
        self.vertices = [
            200,
            50,
            250,
            100,
            250,
            200,
            200,
            250,
            100,
            250,
            50,
            200,
            50,
            100,
            100,
            50,
        ]
        self.canvas.create_polygon(self.vertices, fill="black", outline="gold")
        myfont = tkfont.Font(family="Helvetica", size=24, weight="bold", slant="italic")
        self.canvas.create_text(150, 150, text="Hello World", fill="gold", font=myfont)

        self.canvas.pack()

        tk.mainloop()


# ****************************************************************************************************


def main():
    Polygon()


# ****************************************************************************************************

if __name__ == "__main__":
    main()

# ****************************************************************************************************
