import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server import util


def get_event_get():  # noqa: E501
    """Long Polling Data response after a fixed time

     # noqa: E501


    :rtype: InlineResponse200
    """
    return 'do some magic!'


def register_post(body):  # noqa: E501
    """Register using EventID if present.

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: InlineResponse2001
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
