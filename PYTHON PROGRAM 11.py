print("TAKSHASHILA UNVERSITY")
print(".........................")
print("...........0...........0.....")
print("Student Mark list")
m0=int(input("Enter The python Mark"))
m1=int(input("Enter The DBMS"))
m2=int(input("Enter The ACC"))
Total=m0+m1+m2
print("Total:",Total)
average=Total/3
print("average mark:",average)
if (m0>=50 and m1>=50 and m2>=50):
    print("result:pass")
else:
    print("result:Fail")
if(Total>=250):
    print("GRADE:o GRADE")
            
elif (Total>=200):
    print("GRADE:A++ GRADE")
            
elif (Total>=150):
    print("GRADE:A GRADE")
            
else:
     print("GRADE:B GRADE")
            
            
           
