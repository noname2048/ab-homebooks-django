import logging

from rest_framework.serializers import ModelSerializer

from bookshelves.models import Bookshelf
from accounts.serializers import UserSerializer

import logging

logger = logging.getLogger("bookshelves")


class BookshelfSerializer(ModelSerializer):
    # user = UserSerializer()

    class Meta:
        model = Bookshelf
        fields = ["user", "name"]

    def create(self, validated_data):
        logger.warning("serializer create works")
        bookshelf = Bookshelf(**validated_data)
        request = self.context.get("request", None)
        if request and bookshelf.user is None:
            bookshelf.user = request.user.id
        bookshelf.save()
        return bookshelf
