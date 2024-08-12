# Email tool

This is a simple email tool that sends emails to a list of recipients. It is written in Python and uses the smtplib
library to send emails.

The `MailSender` class is from [Luca Mungo](https://github.com/lucamungo/).

## Installation

Clone the repository and install using pip.

```bash
pip install .
```

## Usage and setup

Create a .env file at the root of your project that has the relevant data for the email tool.

```bash
PASSWORD=your_password
EMAIL=your_email
SMTP_SERVER=your_smtp_server
SMTP_PORT=your_smtp_port
```

I do not recommend using your actual password for this. With Google Mail services you can set up
an app password that you can use for this purpose only and that only allows access to sending emails.

Then, you can use the email tool as follows, in a file called your_file.py

```python
import time
from email_tool import send_email, get_time

start_time = get_time()

chron_start = time.time()
time.sleep(15)
chron_end = time.time()

end_time = get_time()

run_time = chron_end - chron_start

msg = f"""
Script started at {start_time} and ended at {end_time}.
The script ran for {run_time} seconds.
"""

send_email(msg=msg,
           header="Script finished running",
           recipient="you@email.com")
```

and you will receive an email with a message that looks like 

```
Script in file: /path/to/your_file.py

Script started at 08/08/2024 11h54:17 Europe/Paris and ended at 08/08/2024 11h54:32 Europe/Paris.
The script ran for 15.004801034927368 seconds.

End.
```

The `get_time` function is a helper function that returns the current time in a human-readable format with an attached
timezone, which is Europe/Paris by default. You can change the timezone by passing a string to the `timezone` argument.


There is also a context manager built on top called `EmailMonitor`. The point of this is to be able to
send emails if the script finishes with an error, with the trace of the error. Here is an example of how to use it:

```python

from email_tool import EmailMonitor

with EmailMonitor(msg="Default message if no error",
                    header="message",
                    recipient="you@email.com"):
    pass
```

with this, no error will be raised, and you will receive an email with the message "Default message if no error",
along with the time corresponding to the exit of the context manager. You can pass a `timezone` argument to the context
manager to change the timezone, which is Europe/Paris by default.

Instead, if you run the following code:

```python
from email_tool import EmailMonitor

with EmailMonitor(msg="Default message if no error",
                    header="message",
                    recipient="you@email.com"): 
    raise ValueError("This is an error")
```

you will receive an email with the message "This is an error" and the traceback of the error, along with the time when the script 
stopped because of the error.