import logging


def init_logger():
    # Formatter
    # logging.Formatter.converter = lambda *args: datetime.now(tz=timezone(settings.time_zone)).timetuple()
    simple_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    detailed_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s"
    )

    # ConsoleHandler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(simple_formatter)

    # BasicConfig
    logging.basicConfig(
        level=logging.INFO,
        handlers=(
            console_handler,
        ),
    )
