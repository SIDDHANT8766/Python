def CheckEven(No):
    return (No % 2 == 0)

def Increament(No):
    No = No + 1

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual data is : ",Data)

    FData = list(filter(CheckEven,Data))        # Data is parameter of Check function
    print("Data after filter : ",FData)

    MData = list(map(Increament,FData))         # FData is parameter of Increament function
    print("Data after map is : ",MData)




if __name__ == "__main__":
    main()