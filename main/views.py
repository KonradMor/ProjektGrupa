from django.shortcuts import render

# Create your views here.


def View_to_change(request):
    context = {'welcome': "Hello on our site"}
    return render(request, template_name='index.html', context=context)
