from celery import task
from typing import Dict
from homebooks import celery as homebook_celery
import requests

msa_url = "localhost:7000/search/"


@homebook_celery.app.task
def request_book_info(isbn: str) -> Dict:
    params = {"isbn": isbn}
    res = requests.get(url=msa_url, params=params)
    if res.status_code == 200:
        data: Dict = res.json()
        name = data["name"]
        publisher = data["publisher"]

        ret = {"name": name, "publisher": publisher, "isbn": isbn}
        return ret

    return {"isbn": isbn, "message": "search fails"}
