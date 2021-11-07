"""Classes for melon orders."""

class AbstractMelonOrder():

    def __init__(self, species, qty, order_type, tax, country_code):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax
        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        christmas_price = base_price * 1.5
        if self.order_type == "International" and self.qty <10:
            total = ((1 + self.tax) * self.qty * christmas_price) + 3
        else:
            total = (1 + self.tax) * self.qty * christmas_price

        return total
    
    def mark_shipped(self):
        """Return true when shipped."""        
        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    
class GovernmentMelonOrder(AbstractMelonOrder):
    '''No tax on gov't orders'''
    # tax = 0.0    
    #passed_inspection = 
    def __init__(self):
        super().__init__(species, qty, order_type="Government", tax=0.0)

        self.passed_inspection = False
    
    def mark_inspection(self,passed_inspection):
        self.passed_inspection = True
