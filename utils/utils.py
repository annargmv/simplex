import json
import random

from exceptions import ExchangeRateFromCurrencyError, FrankfurtRateFromCurrencyError, CurrencyCodeRateError
from .enum import ProviderNamesEnum
from requests import get


def __best_rate(from_currency_code, to_currency_code):
    """
    Best rate function that is responsible to calculate the rate. The function handles:
    1. If one of the rates isn not found in one of the api's
    2. If the rate was found in both of the rates
    3. If the rate is the same

    :param from_currency_code: from currency code that is the base code
    :param to_currency_code: to currency code that we want to exchange
    :return: list of rate and provider name
    """
    exchange_rate_list = __get_response_exchange_rate(from_currency_code, to_currency_code)
    frankfuter_rate_list = __get_response_frankfuter_rate(from_currency_code, to_currency_code)

    max_rate = max(exchange_rate_list[0], frankfuter_rate_list[0])
    if max_rate == 0:
        raise CurrencyCodeRateError(to_currency_code)

    if max_rate == exchange_rate_list[0]:
        return [max_rate, exchange_rate_list[1]]
    return [max_rate, frankfuter_rate_list[1]]


def __even_rate(from_currency_code, to_currency_code):
    randomize = random.randrange(1)

    if randomize == 0:
        try:
            return __get_response_for_even_rate(
                func=__get_response_exchange_rate,
                from_currency_code=from_currency_code,
                to_currency_code=to_currency_code
            )
        except Exception:
            return __get_response_for_even_rate(
                func=__get_response_frankfuter_rate,
                from_currency_code=from_currency_code,
                to_currency_code=to_currency_code
            )

    if randomize == 1:
        try:
            return __get_response_for_even_rate(
                func=__get_response_frankfuter_rate,
                from_currency_code=from_currency_code,
                to_currency_code=to_currency_code
            )
        except Exception:
            return __get_response_for_even_rate(
                func=__get_response_exchange_rate,
                from_currency_code=from_currency_code,
                to_currency_code=to_currency_code
            )


def __get_response_exchange_rate(from_currency_code, to_currency_code):
    """
    Responsible to handle the Api call to Exchange Api
    :param from_currency_code: from currency code that is the base code
    :param to_currency_code: to currency code that we want to exchange
    :return: list of rate if found and provider name
    """
    response = get(f'https://api.exchangerate-api.com/v4/latest/{from_currency_code}').content
    response_json = json.loads(response.decode('utf8').replace("'", '"'))

    if response_json and response_json.get("result") != "error":
        rates = response_json.get("rates")

        if to_currency_code in rates:
            return [rates[to_currency_code], ProviderNamesEnum.EXCHANGE_RATE.value]
        return [0, ProviderNamesEnum.EXCHANGE_RATE.value]
    raise ExchangeRateFromCurrencyError(from_currency_code=from_currency_code)


def __get_response_frankfuter_rate(from_currency_code, to_currency_code):
    """
    Responsible to handle the Api call to Frankfuter Api
    :param from_currency_code: from currency code that is the base code
    :param to_currency_code: to currency code that we want to exchange
    :return: list of rate if found and provider name
    """
    response = get(f'https://api.frankfurter.app/latest?from={from_currency_code}').content
    response_json = json.loads(response.decode('utf8').replace("'", '"'))

    if response_json and response_json.get("result") != "error":
        rates = response_json.get("rates")

        if to_currency_code in rates:
            return [rates[to_currency_code], ProviderNamesEnum.FRANKFURTER.value]
        return [0, ProviderNamesEnum.FRANKFURTER.value]
    raise FrankfurtRateFromCurrencyError(from_currency_code=from_currency_code)


def __get_response_for_even_rate(func, from_currency_code, to_currency_code):
    """
    Hanlde the response for even rates.
    :param func: function that called to different api
    :param from_currency_code: from currency code that is the base code
    :param to_currency_code: to currency code that we want to exchange
    :return: list of the response from api call
    """
    response = func(from_currency_code, to_currency_code)
    if response[0] == 0:
        raise CurrencyCodeRateError(to_currency_code)
    return response
