# -*- coding: utf-8 -*
# pylint: disable=unused-import
import json

from six import text_type

from sqlalchemy import Column, CheckConstraint, ForeignKeyConstraint, UniqueConstraint, types
from sqlalchemy.types import Boolean, DateTime, Integer, LargeBinary, UnicodeText
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.schema import ForeignKey

from globaleaks.utils.utility import uuid4
# pylint: enable=unused-import


class JSON(types.TypeDecorator):
    """Stores and retrieves JSON as TEXT."""
    impl = types.UnicodeText

    def process_bind_param(self, value, dialect):
        if value is not None:
            return text_type(json.dumps(value))

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            return json.loads(value)

        return value
