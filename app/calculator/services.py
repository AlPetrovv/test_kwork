import os
from pandas import read_csv, DataFrame
from rest_framework import status
from rest_framework.response import Response


def check_csv(name: str) -> Response | str:
    """
    check csv opening  and values of columns is numbers
    """
    try:
        path = f"calculator/data/{name}"
        if not os.path.isfile(path):
            raise FileNotFoundError
        pd: DataFrame = read_csv(path, sep=';')
        pd[pd.columns].astype(float)
        return path
    except ValueError:
        return Response({"detail": "Columns does not contain only numbers"}, status=status.HTTP_409_CONFLICT)
    except FileNotFoundError:
        return Response({"detail": "file not founded"}, status=status.HTTP_409_CONFLICT)
    except Exception as e:
        return Response({"detail": "something is wrong"}, status=status.HTTP_400_BAD_REQUEST)

