from django.db import models

class PizzaOrder(models.Model):
    HAWAIIAN = 'HI'
    PEPPERONI = 'PE'
    CHEESE = 'CH'
    MEAT = 'MT'
    PIZZA_STYLE_CHOICES = [
        (HAWAIIAN, 'Hawaiian'),
        (PEPPERONI, 'Pepperoni'),
        (CHEESE, 'Cheese'),
        (MEAT, 'Meat')
    ]

    LARGE = 14
    MEDIUM = 12
    SMALL = 8
    PIZZA_SIZE_CHOICES = [
        (LARGE, 'Large'),
        (MEDIUM, 'Medium'),
        (SMALL, 'Small'),
    ]
    customerName = models.CharField(max_length=50)
    timeOfOrder = models.DateField(auto_now_add=True)
    size = models.IntegerField(choices=PIZZA_SIZE_CHOICES)
    style = models.CharField(max_length=2, choices=PIZZA_STYLE_CHOICES)