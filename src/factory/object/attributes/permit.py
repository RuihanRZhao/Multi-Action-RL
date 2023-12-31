
class Permit:
    def __init__(self, pur_permit, sal_permit):
        self.purchase = False
        self.sale = False

    def __repr__(self):
        return f"[Pur: {self.purchase}; Sal: {self.sale}]"
