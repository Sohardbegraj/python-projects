# ✅ Python Project 6: Read & Write CSV and Excel Files 📊📁  

# 📌 Problem Statement:  
# Create a Python script that can read data from a CSV file and write it to an Excel file (and vice versa).

# 🧠 What You'll Learn:  
# - Reading CSV using pandas  
# - Writing Excel files using ExcelWriter  
# - File handling and data manipulation  

# ✅ Python Code:  
 
import pandas as pd

# Read data from CSV
csv_data = pd.read_csv("data.csv")
print("CSV Data:")
print(csv_data)

filtered_data = csv_data[csv_data["Marks"] > 85]
print("\n✅ Filtered Data (Marks > 85):")
print(filtered_data)

sorted_data = csv_data.sort_values(by="Marks", ascending=False)
print("\n📊 Sorted Data (by Marks):")
print(sorted_data)

# Step 4: Select specific columns – only Name & Marks
selected_columns = csv_data[["Name", "Marks"]]
print("\n🔎 Selected Columns (Name, Marks):")
print(selected_columns)

# Step 5: Append new rows
new_students = pd.DataFrame({
    "ID": [6, 7],
    "Name": ["Fiona", "George"],
    "Age": [23, 21],
    "Department": ["Biology", "Economics"],
    "Marks": [81, 95]
})

updated_data = pd.concat([csv_data, new_students], ignore_index=True)
print("\n➕ Data After Appending New Rows:")
print(updated_data)

# Write to Excel
updated_data.to_excel("data_output.xlsx", index=False)

# Read back from Excel
excel_data = pd.read_excel("data_output.xlsx")
print("\nExcel Data:")
print(excel_data)


# 📥 How It Works:  
# - Reads data.csv file  
# - Converts and saves it as an Excel file  
# - Reads the Excel file to confirm successful write

# 🔧 Try modifying:  
# – Add filters or sorting  
# – Select specific columns  
# – Append new rows before saving  

# 💡 Use Cases:  
# – Convert CSV sales reports to Excel  
# – Clean and reformat exported data  
# – Automate data handling tasks  

