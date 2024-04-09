from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from instruments.models import Instrument, InstrumentInventory
from django.db.models import Sum
from gemini.client import get_instrument_ai_bio



def instrument_inventory_update():
    instruments_count = Instrument.objects.all().count()
    instruments_value = Instrument.objects.aggregate(
        total_value = Sum('price')
    )['total_value']
    InstrumentInventory.objects.create(
        instruments_count=instruments_count,
        instruments_value=instruments_value
    )

@receiver(pre_save, sender=Instrument)
def instrument_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        try:
            ai_bio = get_instrument_ai_bio(
                instance.product, instance.model
            )
            if ai_bio:
                instance.bio = ai_bio
            else:
                instance.bio = ''
        except Exception as e:
            instance.bio = ''

@receiver(post_save, sender=Instrument)
@receiver(post_delete, sender=Instrument)
def instrument_post_save_delete(sender, instance, **kwargs):
    instrument_inventory_update()
