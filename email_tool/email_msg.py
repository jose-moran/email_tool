from datetime import datetime

import pytz


def email_msg(msg: str) -> str:
    import inspect

    caller_filename = inspect.stack()[1].filename

    formatted_message = f"""Script in file: {caller_filename}
    
    {msg}
    
    End.
    """

    return formatted_message


def get_time(timezone: str = "Europe/Paris") -> str:
    # Timezone for Paris
    tz = pytz.timezone(timezone)

    # Current time in UTC
    now = datetime.now(tz)

    # Format the datetime as day/month/year hh:mm:ss in 24h format
    formatted_time = now.strftime("%d/%m/%Y %Hh%M:%S")

    return f"{formatted_time} {timezone}"
