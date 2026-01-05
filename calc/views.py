from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.from django.shortcuts import render

def home(request):
    result = None
    error = None

    if request.method == 'POST':
        try:
            a = int(request.POST.get("Num1"))
            b = int(request.POST.get("Num2"))
            ch = request.POST.get("ch")

            if ch == "1":
                result = a + b
            elif ch == "2":
                result = a - b
            elif ch == "3":
                result = a * b
            elif ch == "4":
                result = a / b
            else:
                error = "Invalid operation choice"

        except ValueError:
            error = "Please enter valid numbers"

    return render(request, 'home.html', {'result': result, 'error': error})
