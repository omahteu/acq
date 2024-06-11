from typing import Union


def check_request_data(data: dict, fields: Union[str, list]) -> bool:
    if data:
        if isinstance(fields, str):
            fields = [fields]
        for field in fields:
            if field not in data or data[field] == '':
                return True
        return False
    return True

