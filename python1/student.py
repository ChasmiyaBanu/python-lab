class Student:
    def_init_(self,name,reg_number,marks):
        self.name=name
        self.reg_number=reg_number
        self.marks=marks
        self.average=sum(self.marks)/len(self.marks)
        def _str_(self):
            return f"Name:{self.name},Registration number:{self.reg_number},Marks:{self.marks},Average Marks:{self.average}"
        def main():
            num_students=int(input("enter the number of students:"))
            students_dict={}
            for i in range(1,num_students+1):
                print(f"\n enter the details of student{i}:")
                name=input("Name:")
                reg_number=input("Registration Number:")
                marks=[]
                for j in range(3):
                    mark=float(input(f"enter marks for subject{j+1}:"))
                    marks.append(mark)
                    student=Student(name,reg_number,marks)
                    students_dict[name]={'registration Number':reg_number,'Marks':marks,'Average Marks':student.average}
                    print("\nStudent details:")
                    for name,details in student_dict.items():
                       print(f"\nStudent Name:{name}")
                        for key,value in details.items():
                          print(f"{key}:{value}")
if _name_ == "_main_":
    main()
