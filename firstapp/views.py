from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm


# Create your views here.
# there are two ways to create a view: a function based view and a class based view
# for function based view, define a function, give it a name, and for the parameter pass in request
# request is an object sent by the user when they are using your application
def hello_world(request):
    return HttpResponse("Hello world") # so when the user goes to the address linked with hello world view, we will send a response that sends hello world

# for class based view, work with inheritance
# inherits from the View class
class HelloEthiopia(View):
    def get(self, request):
        return HttpResponse("Hello Ethiopia") # so when the user sends a get request to this view, we will return the HTTP response
 
 # next need to link the view functions and classes to addresses (which is URL mapping)

def home(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST) # request.POST contains the info that the user inputted in the form
        if form.is_valid(): # check validitiy
            form.save() # if valid save to the model
            return HttpResponse("Success")
    return render(request, 'index.html', {'form' : form}) #
    