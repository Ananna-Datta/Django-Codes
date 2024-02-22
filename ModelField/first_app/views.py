from django.shortcuts import render
from first_app.forms import MyForms
# Create your views here.
def home(request):
    if request.method == 'POST':
        form = MyForms(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = MyForms()
    return render(request,'home.html', {'form': form })
