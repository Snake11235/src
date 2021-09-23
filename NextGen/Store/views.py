from django.shortcuts import render

# Create your views here.
from django.views import generic
from oscar.core.loading import get_model

Store = get_model('Store', 'Store')

class StoreListView(generic.ListView):
    model = Store
    template_name = 'store/store_list.html'
    context_object_name = 'store_list'

class StoreDetailView(generic.DetailView):
    model = Store
    template_name = 'Store/Store_details.html'
    context_object_name = 'store'