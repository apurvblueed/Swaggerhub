# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2002(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: int=None, message: str=None):  # noqa: E501
        """InlineResponse2002 - a model defined in Swagger

        :param code: The code of this InlineResponse2002.  # noqa: E501
        :type code: int
        :param message: The message of this InlineResponse2002.  # noqa: E501
        :type message: str
        """
        self.swagger_types = {
            'code': int,
            'message': str
        }

        self.attribute_map = {
            'code': 'Code',
            'message': 'Message'
        }
        self._code = code
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2002':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_2 of this InlineResponse2002.  # noqa: E501
        :rtype: InlineResponse2002
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this InlineResponse2002.

        Message Success/failure Code  # noqa: E501

        :return: The code of this InlineResponse2002.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this InlineResponse2002.

        Message Success/failure Code  # noqa: E501

        :param code: The code of this InlineResponse2002.
        :type code: int
        """

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this InlineResponse2002.

        Describing the Success or Failure of Code  # noqa: E501

        :return: The message of this InlineResponse2002.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this InlineResponse2002.

        Describing the Success or Failure of Code  # noqa: E501

        :param message: The message of this InlineResponse2002.
        :type message: str
        """

        self._message = message
