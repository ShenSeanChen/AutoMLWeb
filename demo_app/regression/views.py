from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from plotly.offline import plot
from plotly.graph_objs import Scatter
import csv, io, codecs
import pip
from django.views import generic
from .forms import  NewDataForm
from regression.models import csvInput
# def install(package):
#     if hasattr(pip, 'main'):
#         pip.main(['install', package])
#     else:
#         pip._internal.main(['install', package])
# install('plotly')


from django.db import models
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
# Create your views here.
Lists = ["EDA", "Linear Regression", "Nonlinear Regression"]

# Create your views here.
def index(request):
    return render(request, "regression/index.html", {
        "Lists": Lists
    })

# from . import forms 

# Upload datasets
def upload_file(request):
    if request.method == 'POST':
        form = NewDataForm(request.POST, request.FILES)
        #request.session['data_uploaded'] = form
        if form.is_valid():
            form.save()
            print('form saved')
            form = form.__dict__
            print('form turned into dict')
            # return HttpResponseRedirect('datatable')
            return HttpResponse(form, content_type='regression/')
            #return JsonResponse({'form': form})
            print('form returned')
    else:
        print('empty data form')
        form = NewDataForm()
    return render(request, 'regression/uploadcsv.html', {'form': form})





class UploadedView(generic.ListView):
    template_name = 'regression/uploaded.html'
    context_object_name = 'data_list'
    def get_queryset(self):
        return csvInput.objects.all()


class DisplayView(generic.DetailView):
    model = csvInput
    template_name = 'regression/display.html'






#This function isn't used rightnow
def load_file(request,name):
    task = csvInput.objects.get(task=name)
    #chunks() instead of using read() ensures that large files don’t overwhelm your system’s memory.
    data = task.csv_file.chunks() 
    if not os.path.isfile(task.csv_file.path):
        raise Exception("file not found.")
    context = {}
    context[task.task] = data
    return render(request,'uploaded.html', context)





    



#def datatable(request):
#    data_uploaded = request.session.get('data_uploaded')
#    print(data_uploaded)

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
