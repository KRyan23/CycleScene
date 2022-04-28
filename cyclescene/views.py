''' Required imports '''
from django.shortcuts import render

''' For handling 404 page not found errors '''
def page_not_found(request, exception):
    return render(request, '404.html', status=404)

''' For handling 400 bad request errors '''
def bad_request(request, exception):
    return render(request, '400.html', status=400)

''' For handling 500 server errors '''
def internal_server_error(request, *args, **argv):
    return render(request, '500.html', status=500)
