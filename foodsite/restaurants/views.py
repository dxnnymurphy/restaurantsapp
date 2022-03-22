from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Restaurant, Cuisine
from .forms import CreateForm
# Create your views here.
def index(request):
    template = loader.get_template('restaurants/index.html')
    restaurants = Restaurant.objects.all()
    context = {'restaurants': restaurants}
    return HttpResponse(template.render(context, request))

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            entry = Restaurant()
            entry.Name = data['Name']
            entry.Location = data['Location']
            entry.URL = data['URL']
            entry.Price = data['Price']
            entry.Rating = data['Rating']
            entry.Image = request.FILES['file']
            entry.save()
            cuisineList = data['Cuisine'].split()
            for cuisineentry in cuisineList:
                cuisineentry = Cuisine()
                cuisineentry.cuisine = entry
                cuisineentry.save()
                entry.Cuisines.add(cuisineentry)
            entry.save()
            return HttpResponseRedirect('thanks/')
    else:
        form = CreateForm()
        context = {'form':  form}
    
    return render(request, 'restaurants/create.html', context)

def confirm(request):
    return render(request, 'restaurants/thanks.html')
