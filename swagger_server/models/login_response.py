# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.access_info import AccessInfo
from swagger_server.models.user_info import UserInfo
from swagger_server import util


class LoginResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, secret_key: str=None, user_info: UserInfo=None, access_info: List[AccessInfo]=None):  # noqa: E501
        """LoginResponse - a model defined in Swagger

        :param secret_key: The secret_key of this LoginResponse.  # noqa: E501
        :type secret_key: str
        :param user_info: The user_info of this LoginResponse.  # noqa: E501
        :type user_info: UserInfo
        :param access_info: The access_info of this LoginResponse.  # noqa: E501
        :type access_info: List[AccessInfo]
        """
        self.swagger_types = {
            'secret_key': str,
            'user_info': UserInfo,
            'access_info': List[AccessInfo]
        }

        self.attribute_map = {
            'secret_key': 'secret_key',
            'user_info': 'user_info',
            'access_info': 'access_info'
        }

        self._secret_key = secret_key
        self._user_info = user_info
        self._access_info = access_info

    @classmethod
    def from_dict(cls, dikt) -> 'LoginResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LoginResponse of this LoginResponse.  # noqa: E501
        :rtype: LoginResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def secret_key(self) -> str:
        """Gets the secret_key of this LoginResponse.

        Token secret key  # noqa: E501

        :return: The secret_key of this LoginResponse.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key: str):
        """Sets the secret_key of this LoginResponse.

        Token secret key  # noqa: E501

        :param secret_key: The secret_key of this LoginResponse.
        :type secret_key: str
        """

        self._secret_key = secret_key

    @property
    def user_info(self) -> UserInfo:
        """Gets the user_info of this LoginResponse.


        :return: The user_info of this LoginResponse.
        :rtype: UserInfo
        """
        return self._user_info

    @user_info.setter
    def user_info(self, user_info: UserInfo):
        """Sets the user_info of this LoginResponse.


        :param user_info: The user_info of this LoginResponse.
        :type user_info: UserInfo
        """

        self._user_info = user_info

    @property
    def access_info(self) -> List[AccessInfo]:
        """Gets the access_info of this LoginResponse.


        :return: The access_info of this LoginResponse.
        :rtype: List[AccessInfo]
        """
        return self._access_info

    @access_info.setter
    def access_info(self, access_info: List[AccessInfo]):
        """Sets the access_info of this LoginResponse.


        :param access_info: The access_info of this LoginResponse.
        :type access_info: List[AccessInfo]
        """

        self._access_info = access_info