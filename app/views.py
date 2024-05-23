from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse({'name': 'Aakash'})

def name(request):
    return HttpResponse('Name is Aakash')

