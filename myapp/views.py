from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# from .forms  import RoomForm
# Create your views here
def index(request):
    return render(request,'index.html')
# def index(request):
#     return render(request,'inner-page.html')
# def index(request):
#   return render(request,'portfolio-details.html')
def index(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.name = 'websites'
    feature1.details = 'our service is very quick'

    feature2 = Feature()
    feature2.id = 2
    feature2.name = 'web applications'
    feature2.details = 'our service is very quick'

    feature5 = Feature()
    feature5.id = 3
    feature5.name = 'cards'
    feature5.details = 'our service is very quick'

    feature3 = Feature()
    feature3.id = 4
    feature3.name = 'Flyers'
    feature3.details = 'our service is very quick'

    feature4 = Feature()
    feature4.id = 5
    feature4.name = 'Mentorship'
    feature4.details = 'our service is very quick'
    features = [feature1, feature2, feature3, feature4, feature5]
    return render(request,'index.html',{'features': features})


