import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Denomination Calculator")
window.geometry("500x500")

# Heading
title = tk.Label(
    window,
    text="Denomination Calculator",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

# Amount label
amount_label = tk.Label(window, text="Enter Amount:")
amount_label.pack()

# Amount entry
amount_entry = tk.Entry(window, width=30)
amount_entry.pack(pady=10)

# Result label
result_label = tk.Label(
    window,
    text="",
    justify="left",
    font=("Arial", 12)
)
result_label.pack(pady=20)


def calculate():
    try:
        amount = int(amount_entry.get())

        denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]

        result = "Denominations:\n\n"

        for note in denominations:
            count = amount // note
            amount = amount % note

            if count > 0:
                result += f"₹{note} : {count}\n"

        result_label.config(text=result)

    except ValueError:
        result_label.config(text="Please enter a valid amount!")


# Calculate button
calculate_button = tk.Button(
    window,
    text="Calculate",
    command=calculate
)
calculate_button.pack(pady=10)

# Run the application
window.mainloop()