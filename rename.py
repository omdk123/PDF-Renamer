import os

# Ye folder ka path hai jahan aapki files rakhi hain
# Ye folder ka path hai jahan aapki files rakhi hain
folder_path = r"D:\PDF Rename"

# Folder mein jaayenge
os.chdir(folder_path)

# Har file ko rename karenge
count = 1
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        new_name = f"Notes_{count}.pdf"
        os.rename(filename, new_name)
        count += 1

print("Sabhi files rename ho gayi!")
