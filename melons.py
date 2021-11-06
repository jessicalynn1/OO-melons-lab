"""Classes for melon orders."""

class AbstractMelonOrder():

    def __init__(self, species, qty, shipped, order_type, tax, country_code):
        self.species = species
        self.qty = qty
        self.shipped = shipped
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
    
    #def mark_shipped_code(self):
    #     """Return the country code."""

    #return self.country_code

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    tax = 0.08

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    tax = 0.17
    
    
    #get_total.total = total + 3 
    # def xmas_total(self):
    #     if self.qty < 10:
    #         super().get_total()

    # def get_total(self):
    #     """Calculate price, including tax."""
    #     if self.qty < 10:
    #         total = total + 3

    #     return total

    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code
