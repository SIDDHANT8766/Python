def EmploayeeInfo(Name, Age, Salary, City):
    print("Name :", Name)
    print("Age :", Age)
    print("Salary :", Salary)
    print("City :", City) 

def main():

    # Keyword Argument
    EmploayeeInfo(Age = 26,Name = "Rahul",City="Pune",Salary=None) # Correct (Salary Imp)

if __name__ == "__main__":
    main()