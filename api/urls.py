from django.urls import path
from .views import score
urlpatterns = [
    path('scores',score.get_score)
]