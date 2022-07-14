"""
...
"""
import json

PATH = r'db.json'


# C:\Users\Capibara\Documents\GitHub\hillel_python_course_beginer\HW_16\task_4\

class CurrencyOperationMixIn:
    """
    Provide main currencies' operation with data in .json file
    """

    def status(self, request: str):
        """
        Method return available money on account
        """
        try:
            with open(PATH, 'r', encoding='ANSI') as json_file:
                data: dict = json.load(json_file)
        except FileNotFoundError:
            return "File Not Found"
        result: str | int = data[request]
        return result

    def exchange(self, currency: str, amount: int) -> list | str:
        """
        Method take a curency and amount and convert specified sum of that currency
        to another currency.
        Returns the amount of currency in the accounts
        """
        with open(PATH, 'r', encoding='ANSI') as json_file:
            data: dict = json.load(json_file)
        rate: int = data['rate']
        uah_account: int = data['uah_account']
        usd_account: int = data['usd_account']
        if currency == 'USD':
            exchange_sum: float = amount * rate  # exchanged sum in second currency
            if uah_account < exchange_sum:
                return f'UNAVAILABLE, REQUIRED BALANCE UAH {exchange_sum}, AVAILABLE {data["uah_account"]}'
            data['usd_account'] += amount
            data['uah_account'] -= exchange_sum

        elif currency == 'UAH':
            rate: float = round((1 / rate), 4)
            exchange_sum: float = amount * rate  # exchanged sum in second currency
            if usd_account < exchange_sum:
                return f'UNAVAILABLE, REQUIRED BALANCE UAH {exchange_sum}, AVAILABLE {data["usd_account"]}'
            data['uah_account'] += amount
            data['usd_account'] -= exchange_sum
        else:
            return f'INVALID CURRENCY {currency}'
        with open(PATH, 'w', encoding='ANSI') as json_file:
            json.dump(data, json_file, indent=2)
        return [exchange_sum, rate]


class ResponserMixIn(CurrencyOperationMixIn):
    """ Class provide main type of response like:
    CURRENCY '$$$': RATE ###, AVAILABLE ####
    EXCHANGE '$$$' ###: USD ####, RATE #####
    """

    def currency_req(self, req_currency: str) -> str:
        """ Response in form:
                 RATE ###, AVAILABLE ####
        """
        rate: int = self.status('rate')
        available_account: dict = {'UAH': self.status('uah_account'),
                                   'USD': self.status('usd_account')}
        try:
            response: int | float = available_account[req_currency]
        except KeyError:
            return f'INVALID CURRENCY {req_currency}'
        return f'RATE {rate}, AVAILABLE {response} {req_currency}'

    def exchange_req(self, req_currency: str, req_amount: int | float) -> str:
        """ Response in form:
                 USD ####, RATE #####
        """
        result = self.exchange(req_currency, req_amount)

        if 'UNAVAILABLE' in result or 'INVALID' in result:
            return result
        amount: int | float = result[0]
        rate: int | float = result[1]
        return f'{req_currency} {amount}, RATE {rate}'


class Operator(ResponserMixIn):
    """
    Class provide simple call currency operation
    """

    def caller(self, request: str, requested: str, amount: int = None) -> str:
        """Method call operation with currency"""

        if request == 'COURSE':
            result: str = self.currency_req(requested)
        elif request == 'EXCHANGE':
            result: str = self.exchange_req(requested, amount)
        else:
            result: str = f'INVALID COMMAND {request}'
        return result
