from django.core.exceptions import ValidationError


def powerplatform_order_validator(value, *args, **kwargs):
    from .models import PowerPlatform as PP
    pp_qs = PP.objects.filter(order=value)
    if pp_qs.exists() and len(pp_qs) > 1:
        raise ValidationError(f'More than one Power Platform Points have same order of {value}')

    return value


def md_order_validator(value):
    from .models import MicrosoftDynamics365 as MD
    md_qs = MD.objects.filter(order=value)
    if md_qs.exists() and len(md_qs) > 1:
        raise ValidationError(f'More than one Microsoft Dynamics 365 solutions have same order of {value}')

    return value
