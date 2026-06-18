
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def analyze_and_predict():
    # 1. Retrieve data from the input fields
    name = name_entry.get().strip()
    age_str = age_entry.get().strip()
    hours_str = hours_entry.get().strip()
    student_class = class_combobox.get()
    board = board_combobox.get()
    subject = subject_combobox.get()

    # 2. Validation: Ensure no fields are left blank
    if not name or not age_str or not hours_str or not student_class or not board or not subject:
        messagebox.showerror("Error", "Please fill in all the details before submitting!")
        return

    try:
        age = int(age_str)
        hours = float(hours_str)
    except ValueError:
        messagebox.showerror("Error", "Age must be a number and Study Hours must be a valid number (e.g., 4 or 4.5)!")
        return

    # 3. Interactive Analysis Formula
    # Start with a base score of 40 marks
    predicted_score = 40

    # Add marks based on hours studied (e.g., 7.5 marks per hour)
    predicted_score += (hours * 7.5)

    # Slight adjustments based on curriculum variations (CBSE vs State Portions)
    if board == "CBSE":
        predicted_score += 2  # Continuous evaluation adjustment
    else:
        predicted_score += 1  # State board structural formatting adjustment

    # Subject difficulty balance factor
    if subject in ["Mathematics", "Science"]:
        predicted_score -= 2  # Complex portions require more rigor
    else:
        predicted_score += 2

    # Restrict score to a logical maximum of 100 and minimum of 0
    predicted_score = min(100, max(0, round(predicted_score)))

    # 4. Generate Personalized Performance Feedback
    if predicted_score >= 90:
        feedback = "Outstanding analysis! Your dedicated study hours match top-tier performance standards."
    elif predicted_score >= 75:
        feedback = "Excellent effort. Mastering complex topics will easily push your score past 90."
    elif predicted_score >= 50:
        feedback = "Good foundation. Try increasing your focus by 1-2 hours daily to boost your rank."
    else:
        feedback = "Requires attention. We highly recommend mapping out your subject portions to build momentum."

    # 5. Display the Analysis Report inside the app window
    report_text = (
        f"--- ANALYSIS REPORT ---\n\n"
        f"Student Name: {name}\n"
        f"Age: {age} | Class: {student_class}\n"
        f"Board Format: {board} | Subject Focus: {subject}\n"
        f"Tracked Performance: {hours} Hours/Day\n\n"
        f"🎯 PREDICTED EXAM SCORE: {predicted_score} / 100\n\n"
        f"Feedback: \"{feedback}\""
    )
    
    result_label.config(text=report_text)
    result_frame.pack(pady=15, fill="x")

# --- UI Setup ---
root = tk.Tk()
root.title("Student Exam Score Predictor")
root.geometry("480x600")
root.configure(bg="#f4f7f6")

# Title Header
title_label = tk.Label(root, text="📊 Exam Score Predictor", font=("Segoe UI", 18, "bold"), bg="#f4f7f6", fg="#2c3e50")
title_label.pack(pady=15)

# Form Container Frame
form_frame = tk.Frame(root, bg="white", padx=20, pady=20, bd=1, relief="solid")
form_frame.pack(pady=10, padx=20, fill="both", expand=True)

# Grid Layout for Inputs
labels_font = ("Segoe UI", 10, "bold")

# Student Name
tk.Label(form_frame, text="Student Name:", font=labels_font, bg="white").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(form_frame, font=("Segoe UI", 10), width=25)
name_entry.grid(row=0, column=1, pady=5, padx=10)

# Age
tk.Label(form_frame, text="Age:", font=labels_font, bg="white").grid(row=1, column=0, sticky="w", pady=5)
age_entry = tk.Entry(form_frame, font=("Segoe UI", 10), width=25)
age_entry.grid(row=1, column=1, pady=5, padx=10)

# Class Select Dropdown
tk.Label(form_frame, text="Class/Grade:", font=labels_font, bg="white").grid(row=2, column=0, sticky="w", pady=5)
class_combobox = ttk.Combobox(form_frame, values=["Class 9", "Class 10", "Class 11", "Class 12"], width=22, state="readonly")
class_combobox.grid(row=2, column=1, pady=5, padx=10)

# Board Selection Dropdown
tk.Label(form_frame, text="Education Board:", font=labels_font, bg="white").grid(row=3, column=0, sticky="w", pady=5)
board_combobox = ttk.Combobox(form_frame, values=["CBSE", "State Board"], width=22, state="readonly")
board_combobox.grid(row=3, column=1, pady=5, padx=10)

# Subject Selection Dropdown
tk.Label(form_frame, text="Subject Focus:", font=labels_font, bg="white").grid(row=4, column=0, sticky="w", pady=5)
subject_combobox = ttk.Combobox(form_frame, values=["Mathematics", "Science", "English", "Social Science"], width=22, state="readonly")
subject_combobox.grid(row=4, column=1, pady=5, padx=10)

# Daily Study Hours
tk.Label(form_frame, text="Daily Study Hours:", font=labels_font, bg="white").grid(row=5, column=0, sticky="w", pady=5)
hours_entry = tk.Entry(form_frame, font=("Segoe UI", 10), width=25)
hours_entry.grid(row=5, column=1, pady=5, padx=10)

# Submit Button
submit_btn = tk.Button(form_frame, text="Analyze & Predict Score", font=("Segoe UI", 11, "bold"), bg="#3498db", fg="white", bd=0, cursor="hand2", command=analyze_and_predict)
submit_btn.grid(row=6, column=0, columnspan=2, pady=20, ipadx=10, ipady=5, sticky="ew")

# Result Display Box (Hidden on startup)
result_frame = tk.LabelFrame(root, text=" Analysis Output ", font=("Segoe UI", 10, "bold"), bg="#f4fbf7", fg="#27ae60", bd=2, padx=15, pady=15)
result_label = tk.Label(result_frame, text="", font=("Segoe UI", 10), bg="#f4fbf7", justify="left", fg="#2c3e50")
result_label.pack()

# Keep window running
root.mainloop()
