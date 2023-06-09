from rest_framework.urls import path
from .views import get_sum, get_amount_problems, get_problem

urlpatterns = [
    path("calculator/do-sum/<str:name>/", get_sum, name="do_sum"),
    path("calculator/amount-problems/", get_amount_problems, name="get_amount"),
    path("calculator/get-problem/<int:pk>/", get_problem, name="get_problem")
]
