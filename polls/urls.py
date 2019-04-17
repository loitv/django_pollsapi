from django.urls import path, re_path
# from .views import poll_detail, polls_list
from .apiviews import PollList, PollDetails, ChoiceList, CreateVote

urlpatterns = [
    # path('polls/', polls_list, name='polls_list'),
    # path('polls/<int:pk>/', poll_detail, name='poll_detail'),
    path('polls/', PollList.as_view(), name="poll_list"),
    path("polls/<int:pk>", PollDetails.as_view(), name="poll_detail"),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name="choice_list"),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name="create_vote"),
]
