from django import forms


class CommentForm(forms.Form):
    your_name = forms.CharField(required=True, widget=forms.TextInput(),)
    blessing = forms.CharField(required=True, widget=forms.Textarea(),)

    def save(self):
        from .models import Comment

        s = Comment.objects.create(
            person_name=self.cleaned_data['your_name'],
            comment=self.cleaned_data['blessing'], )
        s.save()