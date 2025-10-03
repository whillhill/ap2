"""Helper functions for working with A2A Message objects."""

from typing import Any

from pydantic import BaseModel


def find_data_part(
    data_key: str, data_parts: list[dict[str, Any]]
) -> Any | None:
    """Returns the value for the first occurrence of the key in the data parts.

    Args:
      data_key: The key to search for.
      data_parts: The data parts to be searched.

    Returns:
      The value for the first occurrence of the key in the data parts, or None.
    """
    for data_part in data_parts:
        if data_key in data_part:
            return data_part[data_key]

    return None


def find_data_parts(
    data_key: str, data_parts: list[dict[str, Any]]
) -> list[Any]:
    """Returns a list of all values for the given key in the data parts.

    Args:
      data_key: The key to search for.
      data_parts: The data parts to be searched.

    Returns:
      A list of all values for the given key in the data parts.
    """
    data_parts_with_key = []
    for data_part in data_parts:
        if data_key in data_part:
            data_parts_with_key.append(data_part[data_key])

    return data_parts_with_key


def parse_canonical_object(
    data_key: str,
    data_parts: list[dict[str, Any]],
    canonical_object_model: BaseModel,
) -> Any:
    """Converts the data part value for the given key to a canonical object.

    Args:
      data_key: The key to search for.
      data_parts: The data parts to be searched.
      canonical_object_model: The pydantic model of the canonical object.

    Returns:
      The canonical object created from the data part value.
    """
    canonical_object_data = find_data_part(data_key, data_parts)
    if canonical_object_data is None:
        raise ValueError(f'{type(canonical_object_model)} not found.')
    return canonical_object_model.model_validate(canonical_object_data)


