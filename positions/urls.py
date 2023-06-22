from rest_framework.urls import path
from positions.views import ListCreatePositionLevelView, ListCreatePositionView

urlpatterns = [
    path("positions/", ListCreatePositionView.as_view(), name="positions"),
    path("position-levels/", ListCreatePositionLevelView.as_view(), name="position-levels"),
]
