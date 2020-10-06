
class creditCard:
    def __init__(self, cardNo):
        self.cardNo = cardNo

    
    @property
    def company(self):
        comp = None
        if str(self.cardNo).startswith('4'):
            comp = 'Visa Card' 
        elif str(self.cardNo).startswith(('50','67','58','63')):
            comp = 'Maestro Card'
        elif str(self.cardNo).startswith('5'):
            comp = 'Master Card'
        elif str(self.cardNo).startswith('37'):
            comp = 'American Express Card'
        elif str(self.cardNo).startswith('62'):
            comp = 'Unionpay Card'
        elif str(self.cardNo).startswith('6'):
            comp = 'Discover Card'
        elif str(self.cardNo).startswith('35'):
            comp = 'JCB Card'
        elif str(self.cardNo).startswith('7'):
            comp = 'Gasoline Card'
        
        return 'Company : ' +comp
