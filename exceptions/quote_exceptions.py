class ExchangeRateToCurrencyError(Exception):
    """Raised when the there was an error in exchange rate api call"""

    def __init__(self, to_currency_code):
        self.to_currency_code = to_currency_code

        super().__init__(f"ExchangeRateToCurrencyError: The to_current_rate code {self.to_currency_code} not valid.")


class ExchangeRateFromCurrencyError(Exception):
    """Raised when the there was an error in exchange rate api call"""

    def __init__(self, from_currency_code):
        self.from_currency_code = from_currency_code

        super().__init__(f"ExchangeRateFromCurrencyError: The from_current_rate code {self.from_currency_code} not valid.")


class FrankfurtRateToCurrencyError(Exception):
    """Raised when the there was an error in frankfurter rate api call"""

    def __init__(self, to_currency_code):
        self.to_currency_code = to_currency_code

        super().__init__(f"FrankfurtRateToCurrencyError: The to_current_rate code {self.to_currency_code} not valid.")


class FrankfurtRateFromCurrencyError(Exception):
    """Raised when the there was an error in frankfurter rate api call"""

    def __init__(self, from_currency_code):
        self.from_currency_code = from_currency_code

        super().__init__(f"FrankfurtRateFromCurrencyError: The from_current_rate code {self.from_currency_code} not valid.")


class BestRateError(Exception):
    """
    Raised when there was an error in best rate function calculation
    """
    def __init__(self, error):
        self.error = error

        super().__init__(f"BestRateError: There was an error in rate calculation.").with_traceback(self.error)


class ValidationError(Exception):
    """
    Used for query params validations
    """
    def __init__(self, message):
        self.message = message

        super().__init__(self.message)


class CurrencyCodeRateError(Exception):
    """
    User for currency code not found in any api
    """

    def __init__(self, currency_code):
        self.currency_code = currency_code

        super().__init__(f"Currency code {self.currency_code} not found at any Api call")

