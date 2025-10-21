def hide_credit_card(number):
    length = len(number)
    hidden = ((length - 4) * "*" + number[-4:])
    return hidden

if __name__ == "__main__":
    card_number = input("Please Enter Credit Card Number: ")
    hidden_number =  hide_credit_card(card_number)
    print(hidden_number)