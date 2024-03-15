import tkinter as tk
import tkinter.messagebox as msg


class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Main Window")

        # (border style): relief='' flat, raised, sunken, solid, ridge, groove
        # (side): side='' top, bottom, left, right
        # (fill): fill='' x, y, both, none
        # (expand): expand=True, False
        # (external padding): padx=, pady=
        # (anchor): anchor='' n, ne, e, se, s, sw, w, nw, center
        # (internal padding): ipadx=, ipady=
        # (stretch): stretch=True, False
        # (weight): weight=0, 1, 2, 3, 4, 5
        # (minsize): minsize=0, 1, 2, 3, 4, 5
        # self.label = tk.Label(
        #     self.main_window,
        #     text="Hello World!",
        #     bg="red",
        #     fg="white",
        #     relief="raised",
        #     borderwidth=5,
        #     padx=10,
        #     pady=10,
        #     anchor="center",
        #     width=20,
        #     height=5
        # )
        # self.label2 = tk.Label(
        #     self.main_window,
        #     text="Goodbye World!",
        #     bg="blue",
        #     fg="white",
        #     relief="raised",
        #     borderwidth=5,
        #     padx=10,
        #     pady=10,
        #     anchor="center",
        #     width=20,
        #     height=5
        # )

        # frame= creates a frame widget
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # button= creates a button widget
        # command= is used to call a function when the button is clicked
        self.my_button = tk.Button(
            self.main_window, text="Click Me!", command=self.do_something
        )

        self.quit_button = tk.Button(
            self.main_window, text="Quit", command=self.main_window.destroy
        )

        # pack() places the widget in the first available position
        # self.label.pack(side="left")
        # self.label2.pack(side="left")
        self.my_button.pack()
        self.quit_button.pack()
        self.top_frame.pack()
        self.bottom_frame.pack()

        # mainloop() keeps the window open until the user closes it
        tk.mainloop()

    def do_something(self):
        msg.showinfo("Response", "Thanks for clicking the button!")


def main():
    MyGUI()


if __name__ == "__main__":
    main()
