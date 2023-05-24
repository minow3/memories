from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Upload
from django.urls import reverse_lazy
from django.views.generic.list import ListView

# Create your views here.


class ListImageView(ListView):
    model = Upload
    template_name = 'list_image.html'
    context_object_name = 'images'


class UploadImageView(CreateView):
    model = Upload
    fields = ['image', 'content']
    template_name = 'upload_image.html'
    success_url = reverse_lazy('share:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)