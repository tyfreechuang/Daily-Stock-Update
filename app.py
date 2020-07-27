import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), './classes'))
from company_info import Info
from gmail import Gmail
from template_builder import Builder

info = Info()
mail = Gmail()
template = Builder()

stockURL = 'https://cloud.iexapis.com/stable/stock/'
token = 'pk_ba66264a4c39449cb935f7697f232b4e'
symbols = ['AAPL', 'GOOGL', 'AMZN']  # insert your stock symbols here
summary = []
articles = []
companyName = []
exchange = []

try:
    # get latest articles
    for i in symbols:
        summary.append(info.get_summary(i, stockURL, token))
        companyName.append(info.get_company_name(i, stockURL, token))
        exchange.append(info.get_exchange(i, stockURL, token))

    # build jinja2 template
    body = template.build_template(symbols, summary, companyName, exchange)

    # Send email
    mail.send_email(body)

    print('Email sent!')

except Exception as e:
    # print thrown error
    print(str(e))