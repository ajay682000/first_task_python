
'''
    Python Coding Task
    Coded Year: 2023
'''



def calculate_total(marks):
    total = sum(marks)
    return  total

def calculate_overall_total(student_data):
    for rollno, student_list in student_data.items():
        student_list["Total"] = calculate_total(student_list["Marks"])
        student_list["Boost_Score"] = student_list["Total"] + student_list["Attendence_Mark"]

    return student_data


def calculate_attendence_score(attendence):
    if(attendence<=100 and attendence>=95):
        attendence=50
    elif(attendence<94 and attendence>=80):
        attendence=45
    elif(attendence<79 and attendence>=60):
        attendence=40
    elif(attendence<59 and attendence>=50):
        attendence=35
    elif(attendence<=49 and attendence>=40):
        attendence=30
    else:
       attendence=25

    return attendence


def get_rollNo_marks_attendence(names, number_of_students):
    student_data = {}
    for i in range(0,number_of_students):
        rollno,m1,m2,m3,m4,m5,m6, attendence = map(int, input().split())
        attendence_score = calculate_attendence_score(attendence)
        student_name = names[i]
        student_list = {
            "Name": student_name,
            "Marks": [m1,m2,m3,m4,m5,m6],
            "Attendence_Mark": attendence_score
        }

        student_data[rollno] = student_list

    return student_data




def get_names_of_student(number_of_students):
    name = []
    #name
    for i in range(0,number_of_students):
        input_name = input()
        if(len(input_name) < 20):
            formatted_name = input_name
            for i in range(20-len(input_name)):
                formatted_name+=' '
        name.append(formatted_name)
    return name

def input_func():
    number_of_students = int(input())
    names = get_names_of_student(number_of_students)
    student_data = get_rollNo_marks_attendence(names, number_of_students)
    return student_data

def calculate_rank(student_data):
    sorted_data = sorted(student_data.items(), key=lambda x: x[1]["Boost_Score"], reverse=True)
    current_rank = 1 
    current_score = None 
    rank_skip_count = 0 
    for i, (rollno, student_list) in enumerate(sorted_data):
        boost_score = student_list["Boost_Score"]
        if boost_score == current_score:
            student_list["Rank"] = current_rank
            rank_skip_count += 1
            if rank_skip_count >= 2:
                rank_skip_count = 0
                current_rank += 1   
        else:
            current_rank = i + 1 
            student_list["Rank"] = current_rank
            current_score = boost_score
            rank_skip_count = 0 
    return student_data

def print_values(data):
    sorted_data = sorted(data.items(), key=lambda x: x[1]["Rank"])
    for rollno, student_list in sorted_data:
        name = student_list["Name"]
        rollno = rollno
        marks = " ".join(map(str, student_list["Marks"]))
        total = student_list["Total"]
        attendence = student_list["Attendence_Mark"]
        boost_score = student_list["Boost_Score"]
        rank = student_list["Rank"]


        print(f"{name} {rollno} {marks} {total} {attendence} {boost_score} {rank}")



if __name__ == "__main__":
    input_values = input_func()
    total = calculate_overall_total(input_values)
    rank = calculate_rank(total)
    print_values(total)