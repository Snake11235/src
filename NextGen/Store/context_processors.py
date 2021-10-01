from .models import Slider, Logo


def slider_processor(request):
    slider = Slider.objects.filter(status=True)
    return {'slider': slider}

def logo_processor(request):
    logo= Logo.objects.filter()
    return {'logo':logo}