"""Validation logic for PaymentMandate."""

import logging

from ap2.types.mandate import PaymentMandate


def validate_payment_mandate_signature(payment_mandate: PaymentMandate) -> None:
    """Validates the PaymentMandate signature.

    Args:
      payment_mandate: The PaymentMandate to be validated.

    Raises:
      ValueError: If the PaymentMandate signature is not valid.
    """
    # In a real implementation, full validation logic would reside here. For
    # demonstration purposes, we simply log that the authorization field is
    # populated.
    if payment_mandate.user_authorization is None:
        raise ValueError("User authorization not found in PaymentMandate.")

    logging.info("Valid PaymentMandate found.")


