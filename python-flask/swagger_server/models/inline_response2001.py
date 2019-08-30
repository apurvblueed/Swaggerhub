# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2001(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, code: int=None, message: str=None, event_length: float=None, queue_id: float=None):  # noqa: E501
        """InlineResponse2001 - a model defined in Swagger

        :param code: The code of this InlineResponse2001.  # noqa: E501
        :type code: int
        :param message: The message of this InlineResponse2001.  # noqa: E501
        :type message: str
        :param event_length: The event_length of this InlineResponse2001.  # noqa: E501
        :type event_length: float
        :param queue_id: The queue_id of this InlineResponse2001.  # noqa: E501
        :type queue_id: float
        """
        self.swagger_types = {
            'code': int,
            'message': str,
            'event_length': float,
            'queue_id': float
        }

        self.attribute_map = {
            'code': 'Code',
            'message': 'Message',
            'event_length': 'EventLength',
            'queue_id': 'QueueID'
        }
        self._code = code
        self._message = message
        self._event_length = event_length
        self._queue_id = queue_id

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse2001':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1 of this InlineResponse2001.  # noqa: E501
        :rtype: InlineResponse2001
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> int:
        """Gets the code of this InlineResponse2001.

        Message Code  # noqa: E501

        :return: The code of this InlineResponse2001.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code: int):
        """Sets the code of this InlineResponse2001.

        Message Code  # noqa: E501

        :param code: The code of this InlineResponse2001.
        :type code: int
        """

        self._code = code

    @property
    def message(self) -> str:
        """Gets the message of this InlineResponse2001.

        Success or Failure Message  # noqa: E501

        :return: The message of this InlineResponse2001.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message: str):
        """Sets the message of this InlineResponse2001.

        Success or Failure Message  # noqa: E501

        :param message: The message of this InlineResponse2001.
        :type message: str
        """

        self._message = message

    @property
    def event_length(self) -> float:
        """Gets the event_length of this InlineResponse2001.

        Unique ID of a particular Event being accessed  # noqa: E501

        :return: The event_length of this InlineResponse2001.
        :rtype: float
        """
        return self._event_length

    @event_length.setter
    def event_length(self, event_length: float):
        """Sets the event_length of this InlineResponse2001.

        Unique ID of a particular Event being accessed  # noqa: E501

        :param event_length: The event_length of this InlineResponse2001.
        :type event_length: float
        """

        self._event_length = event_length

    @property
    def queue_id(self) -> float:
        """Gets the queue_id of this InlineResponse2001.

        Unique ID of queue inline of the Event being accessed.  # noqa: E501

        :return: The queue_id of this InlineResponse2001.
        :rtype: float
        """
        return self._queue_id

    @queue_id.setter
    def queue_id(self, queue_id: float):
        """Sets the queue_id of this InlineResponse2001.

        Unique ID of queue inline of the Event being accessed.  # noqa: E501

        :param queue_id: The queue_id of this InlineResponse2001.
        :type queue_id: float
        """

        self._queue_id = queue_id
