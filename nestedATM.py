card=input("insert a card ")
if card=="debit":
    print("debit card")
    language=input("enter a language ")
    if language=="english":
        print("selected language english")
        pin=int(input("enter your pin"))
        if pin==1234:
            print("correct pin")
            transiction=input("enter a balance enquiry or withdrawal money ")
            if transiction=="balance enquiry":
                print("10000")
            elif transiction=="withdrawal money":
                print("yes i withdrawal money")
                account=input("enter your account ")
                if account=="saving account":
                    print("yes it is saving account")
                elif account=="current account":
                    print("yes it is your current account")
                    amount=int(input("enter your amount "))
                    if amount>=100 or amount<=10000:
                        print("i can take amount")
                        cash=input("you collect your cash ")
                        if cash=="yes":
                            print("yes i got a cash")
                            receipt=input("you want receipt")
                            if receipt=="yes":
                                print("yes i got receipt")
                            else:
                                print("no receipt")
                        else:
                            print("no cash available")
                    else:
                        print("no amount are there")    
                else:
                    print("no it is not your account")
            else:
                print("low balance")
        else:
            print("wrong pin")
    else:
        print("your language is hindi")
else:
    print("credit card")

