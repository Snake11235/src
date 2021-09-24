from .models import Slider


def slider_processor(request):
    slider = Slider.objects.filter(status=True)
    return {'slider': slider}