import json

from utils import utils, validation
from flask import Blueprint, request, make_response
from exceptions import (
    BestRateError,
    FrankfurtRateToCurrencyError,
    ExchangeRateToCurrencyError,
    ExchangeRateFromCurrencyError,
    FrankfurtRateFromCurrencyError,
    ValidationError
)


quote = Blueprint("quote", __name__)


@quote.route("/quote", methods=["GET"])
def get_quote():
    """
    :return: json with data about the rate exchange(exchange_rate, currency_code, amount, provider_name)
    """
    try:
        from_currency_code = validation.__from_currency_validation(request.args.get("from_currency_code"))
        amount = validation.__amount_validation(request.args.get("amount"))
        to_currency_code = validation.__to_currency_validation(request.args.get("to_currency_code"))
    except ValidationError as e:
        return make_response({
            "message": json.dumps(str(e)),
        }, 403)
    except Exception as e:
        return make_response({
            "message": json.dumps(str(e)),
        }, 400)

    try:
        rate_result = utils.__best_rate(
            from_currency_code=from_currency_code,
            to_currency_code=to_currency_code
        )

        # rate_result = utils.__even_rate(
        #     from_currency_code=from_currency_code,
        #     to_currency_code=to_currency_code
        # )

        if rate_result is not None:
            return {
                "exchange_rate": rate_result[0],
                "currency_code": to_currency_code,
                "amount": float(amount) * rate_result[0],
                "provider_name": "".join(rate_result[1])
            }
        return make_response({
            "message": "Oops something went wrong, please check your query params",
        }, 400)

    except (ExchangeRateFromCurrencyError,
            ExchangeRateToCurrencyError,
            FrankfurtRateToCurrencyError,
            FrankfurtRateFromCurrencyError,
            BestRateError) as e:
        return make_response({
            "message": json.dumps(str(e)),
        }, 400)
    except Exception as e:
        return make_response({
            "message": json.dumps(str(e)),
        }, 400)
