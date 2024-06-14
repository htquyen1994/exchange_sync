# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class CoinInfo(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, symbol: str=None, base: str=None):  # noqa: E501
        """CoinInfo - a model defined in Swagger

        :param symbol: The symbol of this CoinInfo.  # noqa: E501
        :type symbol: str
        :param base: The base of this CoinInfo.  # noqa: E501
        :type base: str
        """
        self.swagger_types = {
            'symbol': str,
            'base': str
        }

        self.attribute_map = {
            'symbol': 'symbol',
            'base': 'base'
        }

        self._symbol = symbol
        self._base = base

    @classmethod
    def from_dict(cls, dikt) -> 'CoinInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The CoinInfo of this CoinInfo.  # noqa: E501
        :rtype: CoinInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def symbol(self) -> str:
        """Gets the symbol of this CoinInfo.

        coin symbol  # noqa: E501

        :return: The symbol of this CoinInfo.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str):
        """Sets the symbol of this CoinInfo.

        coin symbol  # noqa: E501

        :param symbol: The symbol of this CoinInfo.
        :type symbol: str
        """

        self._symbol = symbol

    @property
    def base(self) -> str:
        """Gets the base of this CoinInfo.

        coin base  # noqa: E501

        :return: The base of this CoinInfo.
        :rtype: str
        """
        return self._base

    @base.setter
    def base(self, base: str):
        """Sets the base of this CoinInfo.

        coin base  # noqa: E501

        :param base: The base of this CoinInfo.
        :type base: str
        """

        self._base = base
