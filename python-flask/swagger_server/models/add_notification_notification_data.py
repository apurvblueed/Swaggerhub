# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class AddNotificationNotificationData(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, booking_id: int=None, booking_name: str=None):  # noqa: E501
        """AddNotificationNotificationData - a model defined in Swagger

        :param booking_id: The booking_id of this AddNotificationNotificationData.  # noqa: E501
        :type booking_id: int
        :param booking_name: The booking_name of this AddNotificationNotificationData.  # noqa: E501
        :type booking_name: str
        """
        self.swagger_types = {
            'booking_id': int,
            'booking_name': str
        }

        self.attribute_map = {
            'booking_id': 'BookingID',
            'booking_name': 'BookingName'
        }
        self._booking_id = booking_id
        self._booking_name = booking_name

    @classmethod
    def from_dict(cls, dikt) -> 'AddNotificationNotificationData':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The addNotification_Notification_Data of this AddNotificationNotificationData.  # noqa: E501
        :rtype: AddNotificationNotificationData
        """
        return util.deserialize_model(dikt, cls)

    @property
    def booking_id(self) -> int:
        """Gets the booking_id of this AddNotificationNotificationData.

        Unique Booking ID of a customer  # noqa: E501

        :return: The booking_id of this AddNotificationNotificationData.
        :rtype: int
        """
        return self._booking_id

    @booking_id.setter
    def booking_id(self, booking_id: int):
        """Sets the booking_id of this AddNotificationNotificationData.

        Unique Booking ID of a customer  # noqa: E501

        :param booking_id: The booking_id of this AddNotificationNotificationData.
        :type booking_id: int
        """

        self._booking_id = booking_id

    @property
    def booking_name(self) -> str:
        """Gets the booking_name of this AddNotificationNotificationData.

        The kind of booking being executed  # noqa: E501

        :return: The booking_name of this AddNotificationNotificationData.
        :rtype: str
        """
        return self._booking_name

    @booking_name.setter
    def booking_name(self, booking_name: str):
        """Sets the booking_name of this AddNotificationNotificationData.

        The kind of booking being executed  # noqa: E501

        :param booking_name: The booking_name of this AddNotificationNotificationData.
        :type booking_name: str
        """

        self._booking_name = booking_name
