from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
url_get_amount: str = reverse("get_amount")


def get_url_do_sum(file_name: str) -> str:
    return reverse("do_sum", kwargs={"name": file_name})


def get_url_get_problem(pk: str) -> str:
    return reverse("get_problem", kwargs={"pk": pk})


class ProblemAPITestCase(APITestCase):
    def test_do_sum_and_get_problem(self):
        url = get_url_do_sum("test.csv")
        response: Response = self.client.get(url)
        status_code = response.status_code
        self.assertEqual(status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)

        url = get_url_get_problem("1")
        response: Response = self.client.get(url)
        status_code = response.status_code
        self.assertEqual(status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)

    def test_get_amount(self):
        response: Response = self.client.get(url_get_amount)
        status_code = response.status_code
        self.assertEqual(status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)



