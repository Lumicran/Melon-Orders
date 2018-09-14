"""Classes for melon orders."""
import random
import datetime

class AbstractMelonOrder:
    shipped = False
    flat_fee = 0

    def __init__(self, species, qty, country_code):
        self.species = species
        self.qty = qty
        if self.qty > 100:
            raise TooManyMelonsError("No more than 100 melons!")

        self.country_code = country_code

   # def raise_error(self):
        

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_base_price(self):
        weekday = datetime.datetime.now().weekday()
        hour = datetime.datetime.now().hour

        base_price = random.randint(5, 9)

        if 0 <= weekday <= 5 and 8 <= hour < 11:

            base_price += 4
       
        return base_price

    def get_total(self):
        """Calculate price, including tax."""
        base_price = self.get_base_price()

        if self.species.lower() == "christmas melon":
            base_price = 1.5 * base_price

        total = (1 + self.tax) * self.qty * base_price + self.flat_fee
        return total


class TooManyMelonsError(ValueError):
    """error message for more than 100 melons"""
    pass



class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    
    order_type = "domestic"
    tax = 0.08
    def __init__(self, species, qty):
        super().__init__(species, qty, "USA")


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17 

    def get_flat_fee(self):
        
        if self.qty < 10:
            flat_fee = 3
        return flat_fee

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A melon order by USA government"""

    tax = 0
    order_type = "government"
    passed_inspection = False

    def __init__(self, species, qty):
        super().__init__(species, qty, "USA")


    def mark_inspection(self, passed):
        self.passed_inspection = passed

order = DomesticMelonOrder('watermelon', 110)
print (order)
