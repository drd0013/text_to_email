from django.http import HttpResponse

# Create your views here.


def first_view(request):
    import ipdb; ipdb.set_trace()
    return HttpResponse(200)
