def personal_details():
    name = input("Enter name of a person:")
    age = int(input("Enter the age of a person:"))
    gender = input("Enter the gender of a person:")
    salary = int(input("Enter the salary of a person:"))
    state = input("Enter the residing state of a person ")
    city = input("Enter the city of a person")
    print("Name:{}\nAge:{}\nGender:{}\nSalary:{}\nState:{}\nCity:{}".format(name, age,gender,salary,state,city))

personal_details()