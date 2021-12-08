class creditCard:
    def __init__(self, cardNo):
        self.cardNo = cardNo

    @property
    def company(self):
        comp = None
        if str(self.cardNo).startswith("4"):
            comp = "Visa Card"
        elif str(self.cardNo).startswith(("50", "67", "58", "63")):
            comp = "Maestro Card"
        elif str(self.cardNo).startswith("5"):
            comp = "Master Card"
        elif str(self.cardNo).startswith("37"):
            comp = "American Express Card"
        elif str(self.cardNo).startswith("62"):
            comp = "Unionpay Card"
        elif str(self.cardNo).startswith("6"):
            comp = "Discover Card"
        elif str(self.cardNo).startswith("35"):
            comp = "JCB Card"
        elif str(self.cardNo).startswith("7"):
            comp = "Gasoline Card"

        return "Company : " + comp


# create first Check
def firstCheck(self):
    if 13 <= len(self.cardNo) <= 19:
        message = "First check : valid items in length"

    else:
        message = "First check : check card number be of 13 or 16 digits long"

    return message


def validate(self):
    sum_ = 0
    cardNo_ = self.cardNo[::-1]
    for i in range(len(cardNo_)):
        if i % 2 == 1:
            doubleIt = int(cardNo_[i]) * 2
            if len(str(doubleIt)) == 2:
                sum_ += sum([eval(i) for i in str(doubleIt)])
            else:
                sum_ += doubleIt
        else:
            sum_ += int(cardNo_[i])

    if sum_ % 10 == 0:
        response = "Valid Card"
    else:
        response = "Invalid Card"

    return response


@property
def checksum(self):
    return "#CHECKSUM : " + self.cardNo_[-1]


@classmethod
def setCard(cls, cardToCheck):
    return cls(cardToCheck)


card_number = input()
card = creditCard.setCard(card_number)
print(card.company)
print("Card :", card.cardNo_)
print(card.firstCheck())
print(card.checksum)
print(card.validate())
