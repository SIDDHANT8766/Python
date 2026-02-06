
def Phoenix():
    print("Inside Phoenix")

    def zara():
        print("Inside zara")

def main():
    Phoenix.zara()            # Error

if __name__ == "__main__":
    main() 
