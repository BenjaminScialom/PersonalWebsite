from django.shortcuts import render
from website.models import Testimonial


# Create your views here.
def home(request):
    testimonial_list = Testimonial.objects.all()
    context_dict = {'categories': testimonial_list}
    return render(request, 'home.html', {})
