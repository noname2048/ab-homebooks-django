from django.db import models
from django.utils.translation import gettext_lazy as _

from bookshelves.models import Bookshelf


class Book(models.Model):
    """
    현존하는 책정보. 누군가의 책장에 반드시 수록되어있어야 합니다.
    가장중요한 ISBN 정보만을 저장하고,
    이를 이용해 서재정보를 가져옵니다.

    사용자는 우선 ISBN만을 등록하는데, 타 서비스를 이용하여 이 서재정보를 업데이트 합니다.
    ISBN 등록 -> API요청(celery) -> MSA 에서 서재정보 반환 -> 등록
    이 요청은 1분내로 처리되는 것이 좋습니다.

    나중에는 엑셀로도 처리할 수 있도록 로직을 짜 봅시다.

    bookshelf: 실재하는 책장
    user: 책의 주인
    isbn: slug 로 저장되는 13자리
    has_info: 등록대기중(false), 등록완료(true).
    name: 서재 이름 (MSA 반환)
    long_name: 부제목을 포함할경우의 긴 제목(MSA반환)
    publisher: 출판사.
    """

    objects = models.Manager
    bookshelf = models.ForeignKey(Bookshelf, on_delete=models.deletion.CASCADE)
    isbn = models.SlugField(_("isbn"), max_length=50, allow_unicode=False)
    has_info = models.BooleanField(default=False)
    name = models.CharField(_("name"), max_length=100)
    publisher = models.CharField(_("publisher"), max_length=50)
    long_name = models.CharField(_("long_name"), max_length=200, default="")
