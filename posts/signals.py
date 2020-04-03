from django.dispatch import receiver
from django.db.models.signals import pre_save

from .models import PowerPlatform, MicrosoftDynamics365


@receiver(pre_save, sender=PowerPlatform)
def change_powerplatform_order(sender, instance, raw, *args, **kwargs):
    """
    REPLACE OBJECT'S PREVIOUS ORDER WITH NEW
    """
    try:
        prev_obj = PowerPlatform.objects.get(id=instance.id)
        existing_orders = PowerPlatform.objects.filter(order=instance.order)
        if existing_orders.exists() and len(existing_orders) < 2:
            existing_orders.update(order=prev_obj.order)

    except Exception as e:
        print(e)
        return None


# @receiver(pre_save, sender=MicrosoftDynamics365)
def change_md365_order(sender, instance, raw, *args, **kwargs):
    """
    REPLACE OBJECT'S PREVIOUS ORDER WITH NEW
    """
    try:
        prev_obj = MicrosoftDynamics365.objects.get(id=instance.id)
        existing_orders = MicrosoftDynamics365.objects.filter(order=instance.order)
        if existing_orders.exists() and len(existing_orders) < 2:
            existing_orders.update(order=prev_obj.order)

    except Exception as e:
        print(e)
        return None
