# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Body1(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, event_types: List[str]=None):  # noqa: E501
        """Body1 - a model defined in Swagger

        :param event_types: The event_types of this Body1.  # noqa: E501
        :type event_types: List[str]
        """
        self.swagger_types = {
            'event_types': List[str]
        }

        self.attribute_map = {
            'event_types': 'event_types'
        }
        self._event_types = event_types

    @classmethod
    def from_dict(cls, dikt) -> 'Body1':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The body_1 of this Body1.  # noqa: E501
        :rtype: Body1
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event_types(self) -> List[str]:
        """Gets the event_types of this Body1.

        type of event  # noqa: E501

        :return: The event_types of this Body1.
        :rtype: List[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types: List[str]):
        """Sets the event_types of this Body1.

        type of event  # noqa: E501

        :param event_types: The event_types of this Body1.
        :type event_types: List[str]
        """
        if event_types is None:
            raise ValueError("Invalid value for `event_types`, must not be `None`")  # noqa: E501

        self._event_types = event_types
