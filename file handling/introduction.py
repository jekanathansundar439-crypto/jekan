# file handling
# File handling refers to the process of performing operations on a file, such as creating, opening, reading,
#      writing and closing it through a programming interface.
# r (Read Mode):
# Reads the content of the file. The file must exist.
# 👉File-la irukkura content-ah padikkum. File already irukkanum; illa-na error varum.
with open("demo.txt", "r") as file:
    content = file.read()
    print(content)

# w (Write Mode):
# Writes content to the file. If the file doesn't exist, it creates one. Existing content will be overwritten.
# 👉File-ku content write pannum. File illaina create pannum. Already content irundha 
#    atha delete panni pudhusa write pannum.
with open("demo.txt", "w") as file:
    file.write("Hello World")

# a (Append Mode):
# Adds new content at the end of the file without deleting existing content.
# 👉Existing content-ah delete pannama, last-la pudhu content add pannum.
with open("demo.txt", "a") as file:
    file.write("\nNew Line")

# x (Create Mode):
# Creates a new file. If the file already exists, an error occurs.
# 👉Pudhu file create pannum. Already andha file irundha error varum.
with open("index.txt", "x") as file:
    print("File created")

# rb (Read Binary):
# Used for reading binary files like images, videos, PDFs, etc.
# 👉Image, video, PDF madhiri binary files-ah read panna use pannuvom.
with open("image.jpg", "rb") as file:
    data = file.read()

# wb (Write Binary):
# Used for writing binary data.
# 👉Binary data-ah file-ku write panna use pannuvom.

# Reading Methods
# Reads the entire file.
# 👉Motha file content-ah read pannum.
content = file.read()

# readline()
# Reads one line at a time.
# 👉Oru line mattum read pannum.
line = file.readline()

# readlines
# Reads all lines and stores them in a list.
# 👉Ella lines-um list format-la store pannum.
lines = file.readlines()

# Why Use with open()?
# Automatically closes the file after use.
# 👉 Work mudinjadhum file automatic-ah close aagidum. file.close() kudukka thevai illa.
with open("demo.txt", "r") as file:
    print(file.read())

# OS Module Operations
# Changes the file name.
# 👉 File name-ah maathum.
import os
os.rename("demo.txt", "fs.txt")

# Create Folder
# Creates a new folder.
# 👉Pudhu folder create pannum.
os.mkdir("fileSystem")

# Delete File
# Deletes a file.
# 👉File-ah delete pannum.
os.remove("index.txt")

