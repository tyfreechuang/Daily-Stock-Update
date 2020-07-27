import requests


class Info:
    def ___init___(self):
        return

    @staticmethod
    def get_summary(symbol, stock_url, token):
        try:
            # get latest summary of latest article
            response = requests.get(stock_url + symbol + "/news/last/1" + "?token=" + token)
            json = response.json()
            return json[0]['summary']
        except Exception as e:
            # Print thrown error
            print(symbol + ": summary: " + str(e))

    @staticmethod
    def get_articles(symbol, stock_url, token):
        try:
            # get latest article
            response = requests.get(stock_url + symbol + 'news/last/1' + "?token=" + token)
            json = response.json()
            return json[0]['url']
        except Exception as e:
            # print thrown error
            print(symbol + ": articles: " + str(e))

    @staticmethod
    def get_company_name(symbol, stock_url, token):
        try:
            # get company name
            response = requests.get(stock_url + symbol + "/company" + "?token=" + token)
            json = response.json()
            return json['companyName']
        except Exception as e:
            # Print thrown error
            print(symbol + ": company: " + str(e))

    @staticmethod
    def get_exchange(symbol, stock_url, token):
        try:
            # get exchange the stock belongs to
            response = requests.get(stock_url + symbol + '/company' + "?token=" + token)
            json = response.json()
            return json['exchange']
        except Exception as e:
            # print thrown error
            print(symbol + ": exchange: " + str(e))