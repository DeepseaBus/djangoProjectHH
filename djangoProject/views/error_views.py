from django.shortcuts import render


def view_404(request, exception):
    return render(request, 'djangoProject/error_pages/page_404.html', status=404)


def view_500(request):
    return render(request, 'djangoProject/error_pages/page_500.html', status=500)