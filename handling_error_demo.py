filename = input("Enter the file name that you want to open")

try:
    myfile = open(filename,'r')
    for value in myfile:
        print(value)

except FileNotFoundError:
    print("The file does not exist.")

finally:
    print("Your task is completed.")