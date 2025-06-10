"""Repo-specific configuration for stock-alt-options."""

from app.config_shared import *


def get_poller_name() -> str:
    """Return the poller's name for stock-alt-options."""
    return get_config_value("POLLER_NAME", "stock_alt_options")


def get_rabbitmq_queue() -> str:
    """Return the RabbitMQ queue name for stock-alt-options."""
    return get_config_value("RABBITMQ_QUEUE", "stock_alt_options_queue")


def get_dlq_name() -> str:
    """Return the Dead Letter Queue (DLQ) name for stock-alt-options."""
    return get_config_value("DLQ_NAME", "stock_alt_options_dlq")


def get_options_contract_limit() -> int:
    """Return the maximum number of options contracts to process.

    Defaults to 100 if not specified via configuration.
    """
    return int(get_config_value("OPTIONS_CONTRACT_LIMIT", "100"))
