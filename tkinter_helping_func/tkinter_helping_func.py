import tkinter as tk
from tkinter import messagebox

def always_on_top_dialog(dialog_func, *args, **kwargs):
    """
    Opens a Tkinter dialog function with the always-on-top attribute.

    Parameters:
        dialog_func (Callable): The dialog function to call (e.g., messagebox.askyesno or filedialog.asksaveasfilename).
        *args: Positional arguments to pass to the dialog function.
        **kwargs: Keyword arguments to pass to the dialog function.

    Returns:
        Optional[Any]: The result of the dialog function (e.g., True/False for messagebox, str for filedialog).
    """
    # Create a temporary root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.attributes('-topmost', True)  # Set the topmost attribute

    # Call the dialog function with the provided arguments
    result = dialog_func(*args, **kwargs)

    # Destroy the temporary root window
    root.destroy()
    return result

def get_user_input(title: str = "Input Dialog", display_text: str = "Enter your message:", default_value = None, on_close_persist: bool = True):
    """Creates a Tkinter dialog to get user input and returns the entered message."""
    user_message = default_value

    def on_submit():
        nonlocal user_message
        if on_close_persist:
            if entry.get():
                user_message = entry.get()
                root.destroy()
                root.quit()
            else:
                messagebox.showwarning("Input Error", "Please enter a message before submitting.")
        else:
            user_message = entry.get()
            root.destroy()
            root.quit()

    def on_close():
        """Handles the window closing action using the X button."""
        if on_close_persist:
            on_submit()
        else:
            root.destroy()
            root.quit()

    # Create the root window for input
    root = tk.Tk()
    root.title(title)
    root.geometry("400x150")  # Set the window size

    # Create and place the entry field
    tk.Label(root, text=display_text).pack(pady=10)
    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)

    # Create and place the submit button
    tk.Button(root, text="Submit", command=on_submit).pack(pady=10)

    # Bind the Enter key to the submit function
    root.bind('<Return>', lambda event: on_submit())

    # Handle window close event
    root.protocol("WM_DELETE_WINDOW", on_close)

    # Start the Tkinter event loop
    root.mainloop()

    # Return the entered message or None if the window was closed
    return user_message
