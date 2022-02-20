from flask import Flask
from views.quote import quote
from utils.utils import __best_rate

app = Flask(__name__)

app.register_blueprint(quote, url_prefix='/api')
app.register_error_handler(400, __best_rate)


@app.route('/')
def index():
    return f"""Hello, please add query params in order to get an exchange rate result. 
           Add from_currency_code, to_currency_code, amount.
           Currency codes must be 3 capital letters!
           api/quote?from_currency_code=<code>&amount=<amount>&to_currency_code=<code>"""


def main():
    app.run("0.0.0.0", port=3000)


if __name__ == "__main__":
    main()
