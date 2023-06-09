from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Problem
from .serializers import ProblemSerializer
from .services import check_csv
from .tasks import _get_sum


@api_view(["GET"])  # can be POST(without a difference)
def get_sum(request, name: str):
    """
    firstly the file is checked after that  the
    Problem is created then calc sum of every second column
    """
    res: str | Response = check_csv(name)
    if isinstance(res, Response):
        return res
    serializer = ProblemSerializer(data={})
    serializer.is_valid(raise_exception=True)
    problem = serializer.save()
    _get_sum.apply_async(args=(res, problem.id))
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_amount_problems(request):
    amount = Problem.objects.filter(is_active=True).count()
    return Response({"result": amount}, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_problem(request, pk):
    problem = get_object_or_404(Problem, id=pk)
    return Response({"result": problem.amount}, status=status.HTTP_200_OK)
