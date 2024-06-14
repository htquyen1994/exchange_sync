# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.coin_info import CoinInfo
from swagger_server import util


class CoinsResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, coin_list: List[CoinInfo]=None):  # noqa: E501
        """CoinsResponse - a model defined in Swagger

        :param coin_list: The coin_list of this CoinsResponse.  # noqa: E501
        :type coin_list: List[CoinInfo]
        """
        self.swagger_types = {
            'coin_list': List[CoinInfo]
        }

        self.attribute_map = {
            'coin_list': 'coin_list'
        }

        self._coin_list = coin_list

    @classmethod
    def from_dict(cls, dikt) -> 'CoinsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CoinsResponse of this CoinsResponse.  # noqa: E501
        :rtype: CoinsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def coin_list(self) -> List[CoinInfo]:
        """Gets the coin_list of this CoinsResponse.


        :return: The coin_list of this CoinsResponse.
        :rtype: List[CoinInfo]
        """
        return self._coin_list

    @coin_list.setter
    def coin_list(self, coin_list: List[CoinInfo]):
        """Sets the coin_list of this CoinsResponse.


        :param coin_list: The coin_list of this CoinsResponse.
        :type coin_list: List[CoinInfo]
        """

        self._coin_list = coin_list
