from django.shortcuts import render
from django.http import HttpResponse


def get_fibonacci_number(request):
    if request.method == 'POST':
        fibonacci_number = int(request.POST.get('fibonacci_number' , 0))
        counter = 0
        num1 = 1
        num2 = 1
        if fibonacci_number == 0 or fibonacci_number == 1:
            return HttpResponse(
                            f'<p style="color: blue">{fibonacci_number} is in Fibonacci numbers<p/>'
                            '<input class=stana type="button" value="Go back!" onclick="history.back()">'
                            )
        else:
            while counter < fibonacci_number:
                counter = num1 + num2
                num2 = num1
                num1 = counter
            if counter == fibonacci_number:
                return HttpResponse(
                                f'<p style="color: blue">{fibonacci_number} is in Fibonacci numbers<p/>'
                                '<input class=stana type="button" value="Go back!" onclick="history.back()">'
                                )
            else:
                return HttpResponse(
                                f'<p style="color: red">{fibonacci_number} is not in Fibonacci numbers<p/>'
                                '<input class=stana type="button" value="Go back!" onclick="history.back()">'
                                )
    return render(request, 'fibonacci_number.html')
