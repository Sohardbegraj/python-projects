# ✅ *Python Project 7: Read & Write JSON Files* 🔄📄  

# 📌 *Problem Statement:*  
# Create a Python script that reads data from a JSON file, manipulates it, and writes the updated data back to a new JSON file.

# 🧠 *What You'll Learn:*  
# - Working with JSON using Python's `json` module  
# - Parsing nested structures  
# - Reading & writing files  

# ✅ *Python Code:*  
# ```python
import json

# Read JSON file
with open("data.json", "r") as f:
    data = json.load(f)
    print("Original Data:")
    print(data)

# Modify data (example: add a new key)
data["status"] = "processed"

# Write to a new JSON file
with open("updated_data.json", "w") as f:
    json.dump(data, f, indent=4)

print("\nUpdated JSON saved!")
# ```

# 📥 *How It Works:*  
# - Loads `data.json`  
# - Adds or updates values in the dictionary  
# - Writes the updated data to `updated_data.json`

# 🔧 *Try modifying:*  
# – Loop through a list of items  
# – Extract nested values  
# – Merge multiple JSON files  

# 💡 *Use Cases:*  
# – Handling API responses  
# – Config file updates  
# – User data storage  

