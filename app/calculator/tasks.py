from django.shortcuts import get_object_or_404
from pandas import DataFrame, read_csv
from app.celery import app
from calculator.models import Problem
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def _get_sum(path, problem_id: int) -> None:
    logger.info(problem_id)
    logger.info("path" + path)
    problem = get_object_or_404(Problem, pk=problem_id)
    res = None
    try:
        pd: DataFrame = read_csv(path, sep=';')
        pd[pd.columns].astype(float)
        res = sum(pd[pd.columns[::2]].sum())
    except Exception as e:
        return
    finally:
        if not problem:
            return
        if res is None:
            problem.is_active = False
            problem.save(update_fields=["is_active"])
        problem.is_active = False
        problem.amount = res
        problem.save(update_fields=["is_active", "amount"])
