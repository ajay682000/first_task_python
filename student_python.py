
'''
    Python Coding Task
    Coded Year: 2019 - 2020
'''

import operator #for sorting

#initialization in class
class CStudent:
           rollno = 0
           m1 = 0
           m2 = 0
           m3 = 0
           m4 = 0
           m5 = 0
           m5 = 0
           name = ""
           total = 0
           attendence = 0
           boostscore = 0
           
           def __init__ (self, name, rollno, m1, m2, m3, m4, m5, m6, attendence):
              self.name   = name
              self.rollno    = rollno 
              self.m1  = m1
              self.m2  = m2
              self.m3  = m3
              self.m4  = m4
              self.m5  = m5
              self.m6  = m6
              self.total = self.m1 + self.m2 + self.m3 + self.m4 + self.m5 + self.m6
              self.attendence = attendence
              self.boostscore = self.total + self.attendence
              self.rank = 0
              
           
        
           def PrintMarks_Mapping(self):
              print ("name" ,self.name) 
              print ("roll" ,self.rollno) 
              print ("mark", self.marks[0])
              print ("mark", self.marks[1])
              print ("mark", self.marks[2])
              print ("mark", self.marks[3])
              print ("mark", self.marks[4])
              print ("total" , self.total)
              print ("attendence", self.attendence)
              print ("boostscore" , self.boostscore)
              print ("rank", self.rank)

           '''def PrintName(self):
               print (self.name)'''  #for printing list of names first
           #for printing list of student details  
           def PrintMarks(self):
              print (self.name,"\t",self.rollno,"\t",self.m1,"\t",self.m2,"\t",self.m3,"\t",self.m4,"\t",self.m5,"\t",self.m6,"\t",self.total,"\t",self.attendence,"\t",self.boostscore,"\t",self.rank)
           def Rank(self):
               rank = 1
               for i in range(len(studdd)):
                   if(i == 0):
                       studdd[i].rank = 1
                   else:
                       if(studdd[i].boostscore != studdd[i-1].boostscore):
                           rank += 1
                           studdd[i].rank = rank
                       else:
                           studdd[i].rank = rank
                           rank += 1

             
#getting input
print ("Enter Number of Students: ")
maxstudents = int(input())  
studentlist = []
name = []
#name
for i in range(0,maxstudents):
    input_name = input()
    #for printing neatly in order
    if(len(input_name) < 20):
        n_name=input_name
        for i in range(20-len(input_name)):
            n_name+=' '
    name.append(n_name)



#other details
for i in range(0, maxstudents):
   '''details = []
   details = list(map(int, input().split()))'''
   
   
   rollno,m1,m2,m3,m4,m5,m6, attendence = map(int, input().split())

   
   '''print ("Enter rollno: ") 
   rollno = int(input())
   print ("Enter Mark for Subject1: ")
   marks.append(int(input()))
   print ("Enter Mark for Subject2: ")
   marks.append(int(input()))
   print ("Enter Mark for Subject3: ")
   marks.append(int(input()))
   print ("Enter Mark for Subject4: ")
   marks.append(int(input()))
   print ("Enter Mark for Subject5: ")
   marks.append(int(input()))
   print ("Enter Mark for Subject6:")
   marks.append(int(input()))
   print ("Enter the number of days present in 100 days")
   attendence = int(input())'''
   #value for attendence
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
       

   s = CStudent(name[i], rollno, m1, m2, m3, m4, m5, m6, attendence);
   studentlist.append(s)

   

print ("\n")

studdd=sorted(studentlist,key=operator.attrgetter('boostscore'), reverse = True) #sorting in python

#rank calculation
'''rank = 1
for i in range(len(studdd)):
    if(i == 0):
        studdd[i].rank = 1
    else:
        if(studdd[i].boostscore != studdd[i-1].boostscore):
            rank += 1
            studdd[i].rank = rank
        else:
            studdd[i].rank = rank
            rank += 1'''

for i in range(0,len(studdd)):
    studdd[i].Rank()
            
        
    
            


'''print ("Name \n")
print ("Name \t Rollno \t Sub1 \t Sub2 \t Sub3 \t Sub4 \t Sub5 \t Sub6 \t Total \t Atte \t BScore \t Rank")'''
#accessing values to print output
print (studdd[i])
'''for i in range(0, len(studdd)):
    studdd[i].PrintName()'''
for i in range(0, len(studdd)):
    studdd[i].PrintMarks()

#hot report of first 3 students and last 10 students

print("\n")
print("-------------------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------Hot Report-------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------")



for i in range(3):
    studdd[i].PrintMarks()
'''print("\n\n")'''
print("--------------------------------------------------------------------------------------------------------------------")

'''studdd.reverse()'''
for i in range(len(studdd)-1, len(studdd)-11, -1):
    studdd[i].PrintMarks()
print("--------------------------------------------------------------------------------------------------------------------")
print("Enter the choice for searching")
for i in range(100):
    #Searching
    print("1. Register NUmber")
    print("2. Name")
    print("3. Rank")
    print("4. Total")
    print("5. Update the values")
    print("6. Exit")
    choice = int(input("Enter your choice:"))



    #Search by rollno
    if(choice == 1):
        print("Enter the regsiter number to be searched:")
        search_reg_no = int(input())
        found_rno = False
        for i in range(len(studdd)):
            if(studdd[i].rollno==search_reg_no):
                found_rno = True
                studdd[i].PrintMarks()
        if found_rno == False:
            print("Enter the correct number")
        break
    #Search by name
    if(choice == 2):
        print("Enter the name to be searched:")
        search_name = input()
        found_name = False
        for i in range(len(studdd)):
            if search_name.casefold() in studdd[i].name.casefold():
            
                found_name = True
                studdd[i].PrintMarks()
        if(found_name == False):
            print("Enter the correct name")
        break
    #Search by rank
    if(choice == 3):
        print("Enter the rank to be searched:")
        search_rank = int(input())
        found_rank = False
        for i in range(len(studdd)):
            if(studdd[i].rank == search_rank):
                found_rank = True
                studdd[i].PrintMarks()
        if(found_rank == False):
            print("Rank not available")
        break
    #Search by total
    if(choice == 4):
        print("Enter the total to be searched:")
        search_mark = int(input())
        found_mark = False
        for i in range(len(studdd)):
            if(studdd[i].boostscore == search_mark):
                found_mark = True
                studdd[i].PrintMarks()
        if(found_mark == False):
            print("Mark not available")
        break

    
    # Updating the values of student list
    if(choice == 5):
        u_rno=(int(input("Enter the roll number of the student:")))
        found_urno = False
        for i in range(len(studdd)):
            if(studdd[i].rollno==u_rno):
                found_urno = True
                studdd_u = studdd
                studdd_u[i].PrintMarks()
                print("Which field should be changed?")
                print("1. Name")
                print("2. Marks")
                print("3. Attendence")
                update_choice=int(input("Enter your choice:"))
                if(update_choice == 1):
                    update_name = input()
                    if(len(update_name) < 20):
                        for i in range(20-len(update_name)):
                            update_name+=' '
                    studdd_u[i].name = update_name
                    studdd_u[i].PrintMarks()
                    #break
                if(update_choice == 2):
                    print("1. Mark 1")
                    print("2. Mark 2")
                    print("3. Mark 3")
                    print("4. Mark 4")
                    print("5. Mark 5")
                    print("6. Mark 6")
                    update_marks=int(input("Which mark to be changed?:"))
                    if(update_marks == 1):
                        update_m1 = int(input())
                        studdd_u[i].m1 = update_m1
                        studdd_u[i].PrintMarks()
                     #   break
                    if(update_marks == 2):
                        update_m2 = int(input())
                        studdd_u[i].m2 = update_m2
                        studdd_u[i].PrintMarks()
                      #  break
                    if(update_marks == 3):
                        update_m3 = int(input())
                        studdd_u[i].m3 = update_m3
                        studdd_u[i].PrintMarks()
                       # break
                    if(update_marks == 4):
                        update_m4 = int(input())
                        studdd_u[i].m4 = update_m4
                        studdd_u[i].PrintMarks()
                        #break
                    if(update_marks == 5):
                        update_m5 = int(input())
                        studdd_u[i].m5 = update_m5
                        studdd_u[i].PrintMarks()
                      #  break
                    if(update_marks == 6):
                        update_m6 = int(input())
                        studdd_u[i].m6 = update_m6
                        studdd_u[i].PrintMarks()
                       # break
                    #break
                if(update_choice == 3):
                    update_attendence = int(input("Enter the attendence to be changed:"))
                    studdd_u[i].attendence = update_attendence
                    if(update_attendence<=100 and update_attendence>=95):
                        update_attendence=50
                    elif(update_attendence<94 and update_attendence>=80):
                        attendence=45
                    elif(update_attendence<79 and update_attendence>=60):
                        update_attendence=40
                    elif(update_attendence<59 and update_attendence>=50):
                        update_attendence=35
                    elif(update_attendence<=49 and update_attendence>=40):
                        update_attendence=30
                    else:
                        update_attendence=25
                    studdd_u[i].boostscore = update_attendence + studdd_u[i].total
                    studdd1=sorted(studdd_u,key=operator.attrgetter('boostscore'), reverse = True)
                    studdd1[i].PrintMarks()
                    #break
        break
               # if found_urno == False:
                #    print("Enter the correct number")
    #Exit    
    if(choice == 6):
        break
