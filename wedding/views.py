from django.shortcuts import render
from .forms import CommentForm


def home(request):

    is_submit = False
    if request.method == 'POST':
        form = CommentForm(request.POST)
        form_valid = False
        is_submit = True
        if form.is_valid():
            form.save()
            form_valid = True
        return render(request, 'wedding.html',
                      {'form': form, "is_submit": is_submit,
                       "form_valid": form_valid, })
    else:
        form = CommentForm(initial={'your_name': '', 'blessing': ''})

        return render(request, 'wedding.html',
                      {'form': form, "is_submit": is_submit, })