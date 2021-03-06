from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
# from .views import poll_detail, polls_list
from .apiviews import PollList, PollDetails, ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')

urlpatterns = [
    # path('polls/', polls_list, name='polls_list'),
    # path('polls/<int:pk>/', poll_detail, name='poll_detail'),
    # path('polls/', PollList.as_view(), name="poll_list"),
    # path("polls/<int:pk>", PollDetails.as_view(), name="poll_detail"),
    path('polls/<int:pk>/choices/', ChoiceList.as_view(), name="choice_list"),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(), name="create_vote"),
    path('users/', UserCreate.as_view(), name="user_create"),
    path('login/', LoginView.as_view(), name="login"),
]

urlpatterns += router.urls
