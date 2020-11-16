country = input("What country are you from? ")

total = int(input("What is your total order? "))

if country == "canada" or country == "CANADA":
    province = input("What is your province? ")
    if province == "Alberta":
        total = total + (total*0.05)/100
    else:
        if province == "ontario" or province == "new brunswick" or province == "Nova Scotia":
            total = total + (total*0.13)/100
        else:
            total = total + (total*0.06)/100 +(total*0.05)/100
else:
    total = total

print("the total amount with taxes is ",total)

