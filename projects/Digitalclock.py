# ✅ Python Project 5: Digital Clock 🕒  

# 📌 Problem Statement:  
# Build a simple digital clock using Python that updates in real time.

# 🧠 What You'll Learn:  
# - Time manipulation with datetime  
# - Creating GUI with tkinter  
# - Using after() method for live updates  

# ✅ Python Code:  
# python
from tkinter import Label, Tk  
import time  

app = Tk()  
app.title("🕒 Digital Clock")  
app.geometry("300x200")  
app.resizable(False, False)  
app.configure(bg="black")  

clock_label = Label(app, bg="black", fg="white", font=("mono", 20), relief='flat')  
clock_label.pack(pady=20)

date_label = Label(app, bg="black", fg="orange", font=("mono", 20), relief="flat")  
date_label.pack()

def update_time():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%d-%m-%Y") 
    date_label.config(text=current_date)
    clock_label.config(text=current_time)
    clock_label.after(1000, update_time)

update_time()  
app.mainloop()


# 📥 How It Works:  
# - GUI window displays time  
# - Clock updates every 1 second  
# - Simple, clean, and interactive

