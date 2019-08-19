from django.db import models
from django.db import connection
from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.

    """
    created_at = AutoCreatedField()
    modified_at = AutoLastModifiedField()

    class Meta:
        abstract = True


def execute_sql(sql, params=None, keys=None, fetchone=False):
    with connection.cursor() as cursor:
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)

        if fetchone:
            rows = cursor.fetchone()
        else:
            rows = cursor.fetchall()

        if keys:
            result = []
            for row in rows:
                data = dict(zip(keys, row))
                result.append(data)
            return result

        return rows
