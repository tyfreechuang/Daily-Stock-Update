from jinja2 import Environment, FileSystemLoader
from email.mime.text import MIMEText

class Builder:
    def __init__(self):
        return

    @staticmethod
    def build_template(symbols, summary, company_name, exchange):
        try:
            # declare jinja2 template
            file_loader = FileSystemLoader('templates')
            env = Environment(loader=file_loader)
            template = env.get_template('email.html')
            # build jinja2 template from /templates/email.html
            output = template.render(symbols=symbols, summary=summary,
                                     companyName=company_name, exchange=exchange)
            body = MIMEText(output, 'html')

            return body
        except Exception as e:
            # print thrown error
            print(str(e))