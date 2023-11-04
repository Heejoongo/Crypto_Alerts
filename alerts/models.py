from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


class Alert(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, related_name='alerts')
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    base = models.CharField(max_length=10, default='BTC', choices=[(sym, sym) for sym in ['BTC', 'ETH', 'USD', 'EUR']])
    quote = models.CharField(max_length=10, default='USD', choices=[(sym, sym) for sym in ['BTC', 'ETH', 'USD', 'EUR']])
    threshold_value = models.DecimalField(max_digits=20, default=5000, decimal_places=8)
    rate = models.DecimalField(max_digits=20, decimal_places=8, null=True, blank=True)
    warning = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name} - {self.user.username}"

    def clean(self):
        # Custom validation to ensure base_currency and quote_currency are not the same
        if self.base == self.quote:
            raise ValidationError("Base currency and quote currency must be different.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
