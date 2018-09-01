from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values':[ 'Если у Вас остались вопромы, то задавайте их мне по телефогу', '(068) 068-68-68','example@gamil.com']})
