from django.db import models
from django.urls import reverse
from billing.models import BillingProfile

ADDRESS_TYPES = (
    ("billing", "Billing address"),
    ("shipping", "Shipping address"),
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=120, null=True, blank=True, help_text="Shipping to? Who is it for?")
    nickname = models.CharField(max_length=120, null=True, blank=True, help_text="Internal Reference Nickname")
    address_type = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address_line_1 = models.CharField(max_length=120)
    address_line_2 = models.CharField(max_length=120, null=True, blank=True)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=120, default="Mexico")
    state = models.CharField(max_length=120)
    postal_code = models.CharField(max_length=120)

    def __str__(self):
        if self.nickname:
            return str(self.nickname)
        return str(self.address_line_1)
    
    def get_ablote_url(self):
        return reverse("address-update", kwargs={"pk":self.pk})
    
    def get_shot_address(self):
        for_name =self.name
        if self.nickname:
            for_name = "{self.nickname} | {for_name}"
        return "{for_name} {self.address_line_1}, {self.city}"
    
    def get_address(self):
        return "{for_name}\n{self.address_line_1}\n{self.address_line_2}\n{self.city}\n{self.state}, {self.postal_code}\n{country}"