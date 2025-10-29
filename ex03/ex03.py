import os
import datetime

LEVEL_COLORS = {
    "info": 32,
    "debug": 34,
    "warning": 33,
    "error": 31,
}

def smart_log(*args, **kwargs) -> None:
    # Build log message from args
    log_message = ""
    for arg in args:
        if str(arg) == "username":
            arg = os.getlogin()
        log_message += str(arg)

    # Extract options from kwargs
    level = kwargs.get("level")
    log_message = f'[{level.upper()}] ' + log_message if level else log_message

    timestamp = kwargs.get("timestamp")
    date = kwargs.get("date")
    save_to = kwargs.get("save_to")
    colored = kwargs.get("colored")

    if timestamp:
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        log_message = f"{timestamp} {log_message}"

    if date:
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        log_message = f"{date} {log_message}"

    no_color_log_message = log_message
    if colored:
        log_message = f"\033[1;{LEVEL_COLORS.get(level, 37)}m{log_message}\033[0m"
    print(log_message)

    if save_to:
        with open(save_to, "a") as f:
            f.write(no_color_log_message + "\n")


if __name__ == "__main__":
    smart_log("This ", "is an info message.", level="info", timestamp=True, colored=True)
    smart_log("This is a debug message for ", "username", ".", level="debug", date=True, colored=True)
    smart_log("This is a warning message.", level="warning", timestamp=True, date=True, save_to="log.txt", colored=True)
    smart_log("username", ", this is an error message.", level="error", save_to="log.txt", colored=False) 