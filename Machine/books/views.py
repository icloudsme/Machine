from django.shortcuts import render_to_response
from django.template import RequestContext


def customer_list(request):
    return render_to_response('books/photo_list.html', locals(), context_instance=RequestContext(request))