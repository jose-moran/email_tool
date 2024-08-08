import os
from datetime import datetime

import pytz


def email_msg(msg: str) -> str:
    caller_filename = get_importer()

    formatted_message = f"""Script in file: {caller_filename}
    
    {msg}
    
    End.
    """

    return formatted_message


def get_importer():
    import inspect

    # Function to determine if a frame is part of the email_tool package
    def is_internal_caller(_frame):
        module = inspect.getmodule(_frame)
        module_name = module.__name__ if module else ""
        return "email_tool" in module_name

    frame = inspect.currentframe()
    caller_frame = frame

    # Navigate back through the stack to find the first frame not in email_tool
    while caller_frame and is_internal_caller(caller_frame):
        caller_frame = caller_frame.f_back

    # Get the filename from the caller's frame, or default to 'Unknown' if not found
    if caller_frame:
        caller_filename = caller_frame.f_globals.get("__file__", "Unknown")
        caller_filename = os.path.basename(
            caller_filename
        )  # Just the filename, not the full path
    else:
        caller_filename = "Unknown"
    return caller_filename


def get_time(timezone: str = "Europe/Paris") -> str:
    # Timezone for Paris
    tz = pytz.timezone(timezone)

    # Current time in UTC
    now = datetime.now(tz)

    # Format the datetime as day/month/year hh:mm:ss in 24h format
    formatted_time = now.strftime("%d/%m/%Y %Hh%M:%S")

    return f"{formatted_time} {timezone}"
