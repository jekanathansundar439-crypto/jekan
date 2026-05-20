# student data =[{
#                  "name":"mmm"
#                  "gmail" :"aaa@gmail.com"
#                  "mobile": 1234567890
#                  "mark"   :[76,89,70,89,80]
#                }]
# sum the mark of each person
# who mark is high they should me frist they will be rank 1
# second mark rank 2
# message la vanthu rank 1,2,3 exlent should be print,4,5,6 good should be print 

student_data = [
    {
        "name":"jd",
        "mobile":9876543210,
        "email":"jd@gmail.com",
        "mark":[95,99,95,98,90]
    },

    {
        "name":"mugesh",
        "mobile":9123456789,
        "email":"mugesh@gmail.com",
        "mark":[67,74,70,69,72]
    }, 

    {
        "name":"ajay",
        "mobile":9988776655,
        "email":"ajay@gmail.com",
        "mark":[95,91,89,94,96]
    },

    {
        "name":"vishal",
        "mobile":9871234567,
        "email":"vishal@gmail.com",
        "mark":[80,82,79,85,81]
    },

    {
        "name":"tom",
        "mobile":9012345678,
        "email":"nissar@gmail.com",
        "mark":[60,65,70,68,72]
    }
]

#  calculate the total
for s in student_data:
    s["total"] = sum(s["mark"])

# Sort by total marks

for i in range(len(student_data)):

    for j in range(i + 1, len(student_data)):

        if student_data[i]["total"] < student_data[j]["total"]:

            temp = student_data[i]
            student_data[i] = student_data[j]
            student_data[j] = temp


# Assign rank and comments

rank = 1

for s in student_data:

    if s["total"] > 400:
        comment = "Excellent"

    elif s["total"] >= 350:
        comment = "Good"

    else:
        comment = "Average"


    print("Name :", s["name"])
    print("Total :", s["total"])
    print("Rank :", rank)
    print("Comments :", comment)

    print("----------------------")

    rank += 1

 