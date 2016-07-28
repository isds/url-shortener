from .forms import ShirinkForm
from .models import Web_URL
from .util import to_base_62, to_base_10

from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


def shrink_url(request):
    context = {}
    if request.method == 'POST':
        form = ShirinkForm(request.POST)
        if form.is_valid():
            web_url = form.save()
            encoded_string = to_base_62(web_url.id)
            context['short_url']= 'localhost:8000/' + encoded_string
    else:
        form = ShirinkForm()
    context['form'] = form
    return render(request, 'url_shortener/index.html', context)


def redirect(request, id):
    if request.method == 'GET':
        decoded_string = to_base_10(id)
        web_url = get_object_or_404(Web_URL,id=decoded_string)
        web_url.count += 1 # Counts usages
        web_url.save()

        return HttpResponseRedirect(web_url.url)