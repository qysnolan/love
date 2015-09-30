from django.shortcuts import render_to_response


def error_401(request):
    return render_to_response("error_pages/401.html")


def error_403(request):
    return render_to_response("error_pages/403.html")


def error_404(request):
    return render_to_response("error_pages/404.html")


def error_500(request):
    return render_to_response("error_pages/500.html")


def error_502(request):
    return render_to_response("error_pages/502.html")


def error_504(request):
    return render_to_response("error_pages/504.html")


def maintenance(request):
    return render_to_response("error_pages/maintenance.html")


def home(request):

    return render_to_response('home.html')