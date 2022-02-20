from exceptions import ValidationError


def __amount_validation(amount):
    """
    Amount validation. Checks the validity of the value
    :param amount: amount to exchnage
    :return: amount
    """

    if amount is not None and type(amount) == str:
        return amount
    raise ValidationError(message="Oops, something went wrong. Amount must be an str")


def __from_currency_validation(from_currency_rate):
    """
    From currency rate validation. Checks the validity of the value
    :param from_currency_rate: from currency rate code
    :return: currency rate code
    """

    if from_currency_rate is not None and from_currency_rate.isalpha():
        return from_currency_rate
    raise ValidationError(message="Oops, something went wrong. From currency rate must be a str of 3 capital chars and must be passed")


def __to_currency_validation(to_currency_rate):
    """
    To currency rate validation. Checks the validity of the value
    :param to_currency_rate: to currency rate code
    :return: currency rate code
    """
    if to_currency_rate is not None and to_currency_rate.isalpha():
        return to_currency_rate
    raise ValidationError(message="Oops, something went wrong. To currency rate must be a str of 3 capital chars and must be passed")
