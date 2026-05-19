import logging

from configs.log_config import setup_logger

setup_logger()
logger = logging.getLogger(__name__)


def main() -> None:
    logger.info("Hello from hello-jma-xml-py!")


if __name__ == "__main__":
    main()
