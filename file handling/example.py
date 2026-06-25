import os

file=open("jd.txt","r")
content=file.read()
content=file.readline()
print(content)

file=open("jd.txt","w")
mycontent="file handling is working now.."
file.write(mycontent)
print("content updated")

file=open("jd.txt","a")
mydata="\n this is append content"
file.write(mydata)
print("append is working")
file.close()

os.rename("jd.txt","jekan.txt")
print("file name changed successfully")
