from django.shortcuts import render
from django.template.loader import render_to_string
from first_app import forms
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, Users
from first_app.forms import FormClass,Users_form

# Create your views here.
def first_view(request):
    webpage_list = AccessRecord.objects.order_by('date')
    context = {
    'access_records':webpage_list
    }
    return render(request,'first_app/first.html',context)

def users(request):
    form = Users_form()
    if request.method == "POST":
        form = Users_form(request.POST)
        if form.is_valid():
            firstname = form.cleaned_data['firstname']
            lastname = form.cleaned_data['lastname']
            email = form.cleaned_data['email']
            form.save()
    return render(request,'first_app/users_data.html',{'form':form})


def formclass_view(request):
    form = FormClass()
    if request.method == 'POST':
        form = FormClass(request.POST)
        if form.is_valid():
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("address: "+form.cleaned_data['address'])
    return render(request,'first_app/forms_data.html',{'form':form})
