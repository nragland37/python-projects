# ****************************************************************************************************
#
#       This program creates a GUI that converts Celsius to Fahrenheit and vice versa.
#
# ****************************************************************************************************

import tkinter as tk
import tkinter.messagebox as tkmb


class CelsiusGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Temperature Converter")

        # Frames
        self.top_frame = tk.Frame(self.main_window)
        self.mid_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Top Frame - Celsius to Fahrenheit
        self.celsius_label = tk.Label(self.top_frame, text="Celsius: ")
        self.celsius_entry = tk.Entry(self.top_frame, width=20)
        self.celsius_button = tk.Button(
            self.top_frame,
            text="Convert Celsius to Fahrenheit",
            command=self.convert_to_fahrenheit,
        )

        # Mid Frame - Fahrenheit to Celsius
        self.fahrenheit_label = tk.Label(self.mid_frame, text="Fahrenheit: ")
        self.fahrenheit_entry = tk.Entry(self.mid_frame, width=20)
        self.fahrenheit_button = tk.Button(
            self.mid_frame,
            text="Convert Fahrenheit to Celsius",
            command=self.convert_to_celsius,
        )

        # Bottom Frame - Quit button
        self.quit_button = tk.Button(
            self.bottom_frame, text="Quit", command=self.main_window.destroy
        )

        # Packing
        self.celsius_label.pack(side="left", padx=10)
        self.celsius_entry.pack(side="left")
        self.celsius_button.pack(side="left", padx=10)

        self.fahrenheit_label.pack(side="left")
        self.fahrenheit_entry.pack(side="left")
        self.fahrenheit_button.pack(side="left", padx=10)

        self.quit_button.pack()

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    def convert_to_fahrenheit(self):
        try:
            celsius = float(self.celsius_entry.get())
            fahrenheit = (9 / 5) * celsius + 32

            self.fahrenheit_entry.delete(0, tk.END)
            self.fahrenheit_entry.insert(0, str(fahrenheit))
        except ValueError:
            tkmb.showerror(title="Error", message="Enter a number")

    def convert_to_celsius(self):
        try:
            fahrenheit = float(self.fahrenheit_entry.get())
            celsius = (5 / 9) * (fahrenheit - 32)

            self.celsius_entry.delete(0, tk.END)
            self.celsius_entry.insert(0, str(celsius))
        except ValueError:
            tkmb.showerror(title="Error", message="Enter a number")


def main():
    CelsiusGUI()


if __name__ == "__main__":
    main()

# ****************************************************************************************************
