from datetime import datetime, timedelta
import hashlib
import tkinter as tk
from tkinter import ttk, scrolledtext

def generate_hash(current_time):
    hash_object = hashlib.md5(current_time.encode())
    return hash_object.hexdigest()[:8], current_time

def generate_hashes():
    try:
        num_hashes = int(hash_entry.get())
        if num_hashes <= 0:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Please enter a positive number")
            return
    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a valid number")
        return

    output = []
    output.append(f"Generating {num_hashes} hashes with 0.1s delay between each:\n")
    
    current_time = datetime.now()
    result_text.delete(1.0, tk.END)
    
    for i in range(num_hashes):
        current_time_str = current_time.strftime('%Y-%m-%d %H:%M:%S.%f')
        hash_value, timestamp = generate_hash(current_time_str)
        line = f"Hash {i+1}: {hash_value} (Time: {timestamp})"
        output.append(line)
        result_text.insert(tk.END, line + '\n')
        current_time += timedelta(milliseconds=100)
    
    with open("hashes_output.txt", "w") as file:
        file.write("\n".join(output))

# Create main window
root = tk.Tk()
root.title("Hash Generator")
root.geometry("600x400")

# Create and configure frame
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Input field
ttk.Label(main_frame, text="Number of hashes:").grid(row=0, column=0, padx=5, pady=5)
hash_entry = ttk.Entry(main_frame, width=10)
hash_entry.grid(row=0, column=1, padx=5, pady=5)

# Generate button
generate_btn = ttk.Button(main_frame, text="Generate Hashes", command=generate_hashes)
generate_btn.grid(row=0, column=2, padx=5, pady=5)

# Results area
result_text = scrolledtext.ScrolledText(main_frame, width=70, height=20)
result_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Configure grid weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(2, weight=1)
main_frame.rowconfigure(1, weight=1)

if __name__ == "__main__":
    root.mainloop()