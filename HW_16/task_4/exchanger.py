"""
Main module that provide input/output operations
"""
from HW_16.task_4.utils import Operator  # pylint: disable=import-error

REQUEST = Operator().caller


def i_o_operator(request: str) -> str:
    """
    The function parses the input string and calls the appropriate operations
    """
    parsed_req: list = request.split()
    if 'COURSE' in parsed_req and len(parsed_req) == 2:
        case: str = parsed_req[0]
        currency: str = parsed_req[1]
        amount = None
    elif 'EXCHANGE' in parsed_req and len(parsed_req) == 3:
        case: str = parsed_req[0]
        currency: str = parsed_req[1]
        try:
            amount: int = int(parsed_req[2])
        except ValueError:
            return f'INVALID AMOUNT {parsed_req[2]}'
    else:
        return f'INVALID COMMAND {request}'

    result = REQUEST(case, currency, amount)  # noqa
    return result


if __name__ == '__main__':
    # COURSE UAH
    # EXCHANGE UAH 100
    # EXCHANGE USD 100
    while True:
        command: str = input('COMMAND?\n')
        if command == 'STOP':
            print('SERVICE STOPPED')
            break
        print(i_o_operator(command))
