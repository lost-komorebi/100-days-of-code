import requests
import datetime
from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day
# before yesterday then print("Get News").

parameters = {
    "apikey": 'to_fill',
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK
}


def get_price_diff():
    r = requests.get("https://www.alphavantage.co/query", params=parameters)
    r.raise_for_status()
    data = r.json()["Time Series (Daily)"]
    data_list = [{i: data[i]} for i in data.keys()]  # dict转化成list
    price_yesterday = float(list(data_list[0].values())[0]['4. close'])
    price_tdby = float(list(data_list[1].values())[0]['4. close'])
    diff = (price_tdby - price_yesterday) / price_tdby
    if abs(diff) >= 0.05:
        return diff


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces
# for the COMPANY_NAME.
today = datetime.datetime.today().strftime("%Y-%m-%d")
news_para = {
    "q": "Tesla Inc",
    "from": today,
    "sortBy": "popularity",
    "apiKey": "8e07a1e10d624c58b2c14d4a111cde4a"
}


def get_news():
    re = requests.get("https://newsapi.org/v2/everything", params=news_para)
    re.raise_for_status()
    data = re.json()['articles'][:3]
    news = []
    for i in data:
        new = f"Headline:{i['title']} \nBrief:{i['description']}"
        news.append(new)
    return '\n'.join(news)


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's
# title and description to your phone number.

if get_price_diff():
    diff = get_price_diff()
    news = get_news()
    if diff > 0:
        mess_body = f"TSLA: 🔻{diff:.2%}\n{news}"
    else:
        mess_body = f"TSLA: 🔺{diff:.2%}\n{news}"
    # print(mess_body)
    message = client.messages \
        .create(
            body=mess_body,
            from_='to_fill',
            to='to_fill'
        )

    print(message.status)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
