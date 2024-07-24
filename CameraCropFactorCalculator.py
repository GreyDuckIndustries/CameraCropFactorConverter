import tkinter as tk
from tkinter import ttk

def convert_focal_length(focal_length, from_format, to_format):
    crop_factors = {
        'Full Frame': 1.0,
        'APS-C': 1.5,
        'Canon APS-C': 1.6,
        'Micro Four Thirds': 2.0,
        'Fujifilm GFX': 0.79
    }
    full_frame_equivalent = focal_length * crop_factors[from_format]
    converted_focal_length = full_frame_equivalent / crop_factors[to_format]
    return converted_focal_length

def set_format(format, button):
    global selected_format
    selected_format = format
    format_label.config(text=f"Selected Format: {selected_format}")
    convert()
    update_button_colors(button)

def convert():
    try:
        focal_length = float(entry_focal_length.get())
        results = {}
        for to_format in crop_factors.keys():
            if to_format != selected_format:
                results[to_format] = convert_focal_length(focal_length, selected_format, to_format)
        result_text.set("\n".join([f"{format}: {length:.2f}mm" for format, length in results.items()]))
    except ValueError:
        result_text.set("Please enter a valid number for the focal length.")

def update_button_colors(selected_button):
    for button in format_buttons:
        if button == selected_button:
            button.config(style='Selected.TButton')
        else:
            button.config(style='TButton')

# GUI Setup
root = tk.Tk()
root.title("Focal Length Converter")

# Set up styles
style = ttk.Style()
style.configure('TLabel', font=('Arial', 14))
style.configure('TButton', font=('Arial', 12), padding=10)
style.configure('Selected.TButton', background='deepskyblue', foreground='white', font=('Arial', 12, 'bold'), padding=10, borderwidth=2, relief='solid')
style.configure('TFrame', padding="20")

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input fields
ttk.Label(frame, text="Focal Length:").grid(row=0, column=0, sticky=tk.W)
entry_focal_length = ttk.Entry(frame, font=('Arial', 14))
entry_focal_length.grid(row=0, column=1, sticky=(tk.W, tk.E))

# Format Selection Buttons
formats = ["Full Frame", "APS-C", "Canon APS-C", "Micro Four Thirds", "Fujifilm GFX"]
selected_format = formats[0]  # Default format

def create_format_button(format):
    button = ttk.Button(frame, text=format, command=lambda: set_format(format, button))
    return button

format_buttons = []
for i, format in enumerate(formats):
    button = create_format_button(format)
    button.grid(row=1+i, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))
    format_buttons.append(button)

# Format Display
format_label = ttk.Label(frame, text=f"Selected Format: {selected_format}", font=('Arial', 16))
format_label.grid(row=6, column=0, columnspan=2, pady=(10, 10))

# Result display
result_text = tk.StringVar()
ttk.Label(frame, textvariable=result_text, font=('Arial', 14)).grid(row=7, column=0, columnspan=2, pady=(10, 0))

# Make the columns resize properly
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=2)

# Initialize crop factors
crop_factors = {
    'Full Frame': 1.0,
    'APS-C': 1.5,
    'Canon APS-C': 1.6,
    'Micro Four Thirds': 2.0,
    'Fujifilm GFX': 0.79
}

# Set the initial button color
update_button_colors(format_buttons[0])

root.mainloop()
