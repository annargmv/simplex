# Simplex - Currency exchange rate

Hey, Avi
1. In this project I didn't use a DB to store the exchange rates.
2. There are no unit tests because I didn't know how far you wanted from to me go.
3. There are Error handling in the system


In order to tun this project please install requirements

```pip install -r requierments.txt ```


Run the app by running the `main()` in `app.py` or `flask run -p 3000`

##Routs in the system
Run the command `flask routes` in order to see the all possible routes

```
Endpoint         Methods  Rule
---------------  -------  ------------
index            GET      /
quote.get_quote  GET      /api/quote
