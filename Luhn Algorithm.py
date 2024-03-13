def checkNumbers(My_list):
    for elements in My_list:
        try:
            float(elements)
        except ValueError:
            return False
    return True
def sumDigit(MY_list):
    x=0
    for element in MY_list:
        if int(element) > 9:
            x=x+(int(element) - 9 )
        else:
            x=x+int(element)
    return x

while True:
    x=input("Enter credit card number")
    card=list(x)
    if not checkNumbers(card):
        print("enetr a right number")
        continue

    for c in range(0,len(card),2):
        card[c]=int(card[c])*2 
    if sumDigit(card) % 10 ==0:
        print ("valid")
    else:
        print("Not vaild")



