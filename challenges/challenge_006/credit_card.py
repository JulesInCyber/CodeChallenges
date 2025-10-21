def hide_credit_card(number):
    number = str(number)
    length = len(number)
    print((length-4)*"*" + number[-4:])

if __name__ == "__main__":
    card = 1472583698745632
    hide_credit_card(card)
