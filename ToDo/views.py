from ast import Del
from django.shortcuts import render
from django.views import View
from .models import challenge_list_Model
from .forms import challege_list_Form
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


# def index(request):
#     return render(request, "ToDo/index.html")

class index(View):
    def get(self, request):
        form = challege_list_Form()
        challenges_list = challenge_list_Model.objects.all()
        return render(request, "ToDo/index.html", {"form": form, "challenges_list": challenges_list})

    def post(self, request):
        form = challege_list_Form(request.POST)
        challenges_list = challenge_list_Model.objects.all()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main_page'))

        return render(request, "ToDo/index.html", {"form": form, "challenges_list": challenges_list})


def delete_challenge(request, id):
    model = challenge_list_Model.objects.get(id=id)
    model.delete()
    return HttpResponseRedirect(reverse('main_page'))
