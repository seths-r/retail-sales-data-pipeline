import tkinter as tk
from tkinter import filedialog, ttk

# Initialize main window
root = tk.Tk()
root.title("Data Extraction Application")

# Step 1: File Upload Screen
def step1():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="Select File Type:").pack(pady=10)
    
    file_type_var = tk.StringVar()
    file_type_dropdown = ttk.Combobox(root, textvariable=file_type_var)
    file_type_dropdown['values'] = ('PDF', 'Excel', 'TXT')
    file_type_dropdown.current(0)  # set default selection
    file_type_dropdown.pack(pady=10)

    def upload_file():
        file_path = filedialog.askopenfilename()
        tk.Label(root, text=f"File Selected: {file_path}").pack(pady=10)
    
    tk.Button(root, text="Upload File", command=upload_file).pack(pady=10)
    
    tk.Button(root, text="Next", command=step2).pack(pady=20)

# Step 2: Data Schema Selection Screen
def step2():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="Select Data Schema:").pack(pady=10)
    
    schema_var = tk.StringVar(value=[])
    schema_listbox = tk.Listbox(root, listvariable=schema_var, selectmode='multiple')
    schema_options = ['SAMPLE_ID', 'TESTNUMBER', 'TESTNAME', 'VALUE']
    for option in schema_options:
        schema_listbox.insert(tk.END, option)
    schema_listbox.pack(pady=10)
    
    tk.Button(root, text="Next", command=step3).pack(pady=20)

# Step 3: Placeholder for further steps or actions
def step3():
    for widget in root.winfo_children():
        widget.destroy()
    
    tk.Label(root, text="Processing...").pack(pady=20)
    # Further processing can be added here

# Start with the first step
step1()

# Run the application
root.mainloop()
