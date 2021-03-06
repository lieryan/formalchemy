# -*- coding: utf-8 -*-

from formalchemy.helpers import literal

class PkError(Exception):
    """An exception raised when a primary key conflict occur"""

class ValidationError(Exception):
    """an exception raised when the validation failed
    """
    @property
    def message(self):
        return literal.escape(self.args[0])
    def __repr__(self):
        return 'ValidationError(%r,)' % self.message

class FieldNotFoundError(ValidationError):
    """an exception raise when the field is not found in request data"""
