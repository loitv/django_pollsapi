from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from.models import Poll

# Create your views here.

def polls_list(request):
    max_objects = 20
    polls = Poll.objects.all()[:max_objects]
    data = {"results": list(polls.values("question", "created_by__username", "pub_date"))}
    return JsonResponse(data)


def poll_detail(request, pk):
    poll = get_object_or_404(Poll, id=pk)
    print(poll)
    data = {"results": {"question": poll.question,
                        "created_by": poll.created_by.username,
                        "pub_date": poll.pub_date}}
    return JsonResponse(data)