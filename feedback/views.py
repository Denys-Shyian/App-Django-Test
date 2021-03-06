from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FeedbackFrom
from .models import Feedback


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = FeedbackFrom(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            feed = Feedback(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                feedback=form.cleaned_data['feedback'],
                rating=form.cleaned_data['rating'],

            )
            feed.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackFrom()
    return render(request, 'feedback/feedback.html', context={'form': form})


def done(request):
    return render(request, 'feedback/done.html')
