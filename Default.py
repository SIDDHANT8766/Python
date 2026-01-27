def EmploayeeInfo(Name = "Gotya", Age = 21, Salary = 1000, City = "Pune"):
    print("Name :", Name)
    print("Age :", Age)
    print("Salary :", Salary)
    print("City :", City) 

def main():

    #EmploayeeInfo(Age = 26,Name = "Rahul",City="Pune",Salary=2000.50) # Correct
    EmploayeeInfo()

if __name__ == "__main__":
    main()