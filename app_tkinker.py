import tkinter as tk
from tkinter import messagebox
import order_app
import user_name
import display_data

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Single Window Application")
        self.adjust_window()
        self.create_widgets()

    def adjust_window(self):
        window_width = 450
        window_height = 250

        # Get the screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Find the center point
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)

        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    def create_widgets(self):
        tk.Label(self.root, text="Please enter a string:", font=('Arial', 14)).pack(pady=10)

        self.input_entry = tk.Entry(self.root, width=30, font=('Arial', 14))
        self.input_entry.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        button1 = tk.Button(button_frame, text="Create Image", width=12, height=2, command=self.button1_action, font=('Arial', 12))
        button1.pack(side=tk.LEFT, padx=10)

        button2 = tk.Button(button_frame, text="Fill Excel", width=12, height=2, command=self.button2_action, font=('Arial', 12))
        button2.pack(side=tk.LEFT, padx=10)

    def button1_action(self):
        user_input = self.input_entry.get()
        data = user_name.extract_dishes_and_quantities(user_input)
        display_data.display_data(data)

    def button2_action(self):
        user_input = self.input_entry.get()
        try:
            user_list = user_name.return_list_name(user_input)
            file_path = "C:\\Users\\PC\\Desktop\\customer_test.xlsx"
            order_app.auto_fill(user_list, file_path)
            messagebox.showinfo("Button 1", "Completed fill Excel successfully!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
