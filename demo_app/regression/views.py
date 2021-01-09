from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

import csv, io, codecs
import pip
# def install(package):
#     if hasattr(pip, 'main'):
#         pip.main(['install', package])
#     else:
#         pip._internal.main(['install', package])
# install('plotly')


from django.db import models
from django.shortcuts import render
from django.contrib import messages
# Create your views here.
Lists = ["EDA", "Linear Regression", "Nonlinear Regression"]

# Create your views here.
def index(request):
    return render(request, "regression/index.html", {
        "Lists": Lists
    })

# from . import forms 
from .forms import  NewDataForm

# Upload datasets
def upload_file(request):
    if request.method == 'POST':
        form = NewDataForm(request.POST, request.FILES)
        request.session['data_uploaded'] = form
        if form.is_valid():
            form.save()
            print('form saved')
            form = form.__dict__
            print('form turned into dict')
            # return HttpResponseRedirect('datatable')
            return HttpResponse(form, content_type='regression/')
        print('we just did redirect')
    else:
        print('empty data form')
        form = NewDataForm()
    return render(request, 'regression/uploadcsv.html', {'form': form})

def datatable(request):
    data_uploaded = request.session.get('data_uploaded')
    print(data_uploaded)

# client side validation
# class NewDataForm(forms.Form):
# class NewDataForm(forms.ModelForm):
#     task = forms.CharField(label="New Task")
#     csv_file = forms.FileField(label="New CSV", widget=forms.FileInput(attrs={'accept': ".csv"}))
#     # priority = forms.IntegerField(label="Priority", min_value=1, max_value=5)

# public_data = []

# def uploadcsv(request):
#     # also make sure server side validation
#     if request.method == "POST":
#         form = NewDataForm(request.POST, request.FILES)
#         if form.is_valid():
#             # 
#             form.save()
#             # task = form.cleaned_data['task']
#             Lists.append(task)
            
#             csv_file = form.cleaned_data["csv_file"]
#             # print('Here is the csv file uploaded: ', csv_file)
#         #    public_data.append(csv_file)
#         #    print('task: ', task)
            
#         #    print('hahaha: ', public_data)
#         else:
#             return render(request, "regression/uploadcsv.html", {
#                 "form": form
#             })

#     return render(request, "regression/uploadcsv.html", {
#         "form": NewDataForm()
#     })

# print(public_data)
# def uploadcsv(request):
#     print(request.POST)
#     if request.POST and request.FILES:
#         csvfile = request.FILES['csv_file']
#         dialect = csv.Sniffer().sniff(codecs.EncodedFile(csvfile, "utf-8").read(1024))
#         csvfile.open()
#         reader = csv.reader(codecs.EncodedFile(csvfile, "utf-8"), delimiter=',', dialect=dialect)

#     return render(request, "regression/eda.html", locals())

# EDA

# def plot(request):
#     username = request.POST['csv_file']
#     sns.pairplot(username)
#     return render(request, "regression/plot.html")

from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

def eda(request):
    if request.POST:
        # csv_file = request.POST
        plot_div = plot([Scatter(x=csv_file.iloc[:,0], y=csv_file.iloc[:,1],
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')

    else:
        x_data = [0,1,2,3,4,5]
        y_data = [x**2 for x in x_data]
        plot_div = plot([Scatter(x=x_data, y=y_data,
                            mode='lines', name='test',
                            opacity=0.8, marker_color='green')],
                output_type='div')
    return render(request, "regression/eda.html", context={'plot_div': plot_div})

# Regression Analysis
