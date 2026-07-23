"""
Main application entry point.
"""

from constants import WELCOME_MESSAGE
from logger import logger
from utils import current_time, print_banner


def main() -> None:
    """Run the application."""

    print_banner()

    logger.info("Application started.")

    print(WELCOME_MESSAGE)

    print(f"Current Time: {current_time()}")

    logger.info("Application finished.")


if __name__ == "__main__":
    main()
