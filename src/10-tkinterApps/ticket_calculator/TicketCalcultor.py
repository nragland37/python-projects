# ****************************************************************************************************
#
#       This program creates a GUI that calculates the total charges for tickets based on the ticket
#       type and number of tickets.
#
# ****************************************************************************************************

import tkinter as tk
import tkinter.messagebox as tkmb

# ****************************************************************************************************


class TicketCalculatorGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Ticket Calculator")

        # Frames
        self.top_frame = tk.Frame(self.main_window)
        self.mid_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)

        # Top Frame - Ticket Category Radio Buttons
        self.ticket_type = tk.StringVar()
        self.ticket_type.set("adult")
        self.senior_radio = tk.Radiobutton(
            self.top_frame,
            text="Senior (>65)",
            variable=self.ticket_type,
            value="senior",
        )
        self.adult_radio = tk.Radiobutton(
            self.top_frame,
            text="Adult (15-65)",
            variable=self.ticket_type,
            value="adult",
        )
        self.child_radio = tk.Radiobutton(
            self.top_frame,
            text="Child (5-15)",
            variable=self.ticket_type,
            value="child",
        )

        # Mid Frame - Entry  of Tickets
        self.num_tickets_label = tk.Label(
            self.mid_frame, text="Enter the number of tickets: "
        )
        self.num_tickets_entry = tk.Entry(self.mid_frame, width=10)

        # Bottom Frame - Calculate,Quit
        self.calculate_button = tk.Button(
            self.bottom_frame, text="Display Charges", command=self.calculate_price
        )
        self.quit_button = tk.Button(
            self.bottom_frame, text="Quit", command=self.main_window.destroy
        )

        # Packing
        self.senior_radio.pack(side="top")
        self.adult_radio.pack(side="top")
        self.child_radio.pack(side="top")

        self.num_tickets_label.pack(side="left")
        self.num_tickets_entry.pack(side="left")

        self.calculate_button.pack(side="left")
        self.quit_button.pack(side="left")

        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()

        tk.mainloop()

    # ************************************************************************************************

    def calculate_price(self):
        try:
            num_tickets = int(self.num_tickets_entry.get())

            if num_tickets < 0:
                raise ValueError

            ticket_price = {"senior": 7, "adult": 12, "child": 5}
            total_price = num_tickets * ticket_price[self.ticket_type.get()]
            tkmb.showinfo("Total Price", f"Your total charges = ${total_price:.2f}")
        except ValueError:
            tkmb.showerror(title="Error", message="Enter a positive round number")


# ****************************************************************************************************


def main():
    app = TicketCalculatorGUI()


# ****************************************************************************************************

if __name__ == "__main__":
    main()

# ****************************************************************************************************