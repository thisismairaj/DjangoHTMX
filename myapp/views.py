from django.shortcuts import render
from .models import Person
from .forms import PersonForm
from .filters import PersonFilter

def index(request):
  query = request.GET
  person_filter = PersonFilter(request.GET, queryset=Person.objects.all())
  context = {
    'search_form': person_filter.form,
    'person_form': PersonForm,
    'results': person_filter.qs,
    'results_count': len(person_filter.qs),
    'persons': Person.objects.all().order_by('-id')[:10],
    'query': query
  }
  
  return render(request, 'index.html', context)

def create(request):
  context = {
    'person_form': PersonForm
  }
  if request.method == "POST":
    form = PersonForm(request.POST or None)
    print(form)
    if form.is_valid():
      person = form.save()
      context = {'person': person}
      return render(request, 'partials/person.html', context)

  return render(request, 'partials/form.html', context)