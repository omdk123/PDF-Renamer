import os

folder_path = r"D:\PDF Rename"

os.chdir(folder_path)

# every file will be renamed
count = 1
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf"):
        new_name = f"Notes_{count}.pdf"
        os.rename(filename, new_name)
        count += 1

print("all files are remnamed!")
