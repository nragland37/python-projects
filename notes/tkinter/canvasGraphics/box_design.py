import tkinter as tk


class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Canvas Practice")

        self.canvas = tk.Canvas(self.main_window, width=300, height=300)

        self.canvas.create_rectangle(0, 0, 300, 300, fill="black")

        self.canvas.create_rectangle(25, 25, 275, 275, fill="white")
        self.canvas.create_line(25, 25, 275, 275, fill="black")
        self.canvas.create_line(275, 25, 25, 275, fill="black")

        self.canvas.create_rectangle(50, 50, 250, 250, fill="black")
        self.canvas.create_line(50, 50, 250, 250, fill="white")
        self.canvas.create_line(250, 50, 50, 250, fill="white")

        self.canvas.create_rectangle(75, 75, 225, 225, fill="white")
        self.canvas.create_line(75, 75, 225, 225, fill="black")
        self.canvas.create_line(225, 75, 75, 225, fill="black")

        self.canvas.create_rectangle(100, 100, 200, 200, fill="black")
        self.canvas.create_line(100, 100, 200, 200, fill="white")
        self.canvas.create_line(200, 100, 100, 200, fill="white")

        self.canvas.create_rectangle(125, 125, 175, 175, fill="white")
        self.canvas.create_line(125, 125, 175, 175, fill="black")
        self.canvas.create_line(175, 125, 125, 175, fill="black")

        self.canvas.create_rectangle(150, 150, 150, 150, fill="black")
        self.canvas.create_line(150, 150, 150, 150, fill="white")
        self.canvas.create_line(150, 150, 150, 150, fill="white")

        self.canvas.create_rectangle(175, 175, 125, 125, fill="black")
        self.canvas.create_line(175, 175, 125, 125, fill="white")
        self.canvas.create_line(125, 175, 175, 125, fill="white")

        self.canvas.create_line(0, 0, 300, 300, fill="white")
        self.canvas.create_line(300, 0, 0, 300, fill="white")
        self.canvas.create_line(150, 0, 150, 300, fill="white")
        self.canvas.create_line(0, 150, 300, 150, fill="white")
        self.canvas.create_line(0, 0, 300, 300, fill="white")
        self.canvas.create_line(25, 0, 25, 300, fill="white")
        self.canvas.create_line(275, 0, 275, 300, fill="white")
        self.canvas.create_line(0, 25, 300, 25, fill="white")
        self.canvas.create_line(0, 275, 300, 275, fill="white")
        self.canvas.create_line(0, 75, 300, 75, fill="white")
        self.canvas.create_line(0, 225, 300, 225, fill="white")
        self.canvas.create_line(75, 0, 75, 300, fill="white")
        self.canvas.create_line(225, 0, 225, 300, fill="white")
        self.canvas.create_line(0, 125, 300, 125, fill="white")
        self.canvas.create_line(0, 175, 300, 175, fill="white")
        self.canvas.create_line(125, 0, 125, 300, fill="white")
        self.canvas.create_line(175, 0, 175, 300, fill="white")
        self.canvas.create_line(0, 150, 300, 150, fill="white")

        self.canvas.pack()

        tk.mainloop()


def main():
    MyGUI()


if __name__ == "__main__":
    main()
