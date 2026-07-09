"""Custom `StructValue` classes"""

import math
import random
from typing import Any, Dict, List, Literal, Optional, override

from django.utils.http import urlencode
from wagtail.blocks import StructValue

NUMBER_OF_BYTES = 5


AlertLevel = Literal["info", "success", "warning", "error"]
AlertIcon = Literal[
    "info", "circle-check", "alert-triangle", "x-circle", "question-mark-circle"
]


def rand_str(n: int) -> str:
    """
    Generate random string form random bytes after converting to hex.

    Args:
        n (int): Number of bytes used to generate random `n` bytes.

    Returns:
        str: Random string.
    """

    return random.randbytes(n).hex()


class NameMixin:
    """A mixin that provides a `name` property."""

    prefix: str

    @property
    def input_name(self) -> str:
        """
        Random `name` used in input names.

        Returns:
            str: Random string.
        """

        return f"{self.prefix}-{rand_str(NUMBER_OF_BYTES)}"

    @override
    def get_context(  # type: ignore
        self,
        value: Dict[str, Any],
        parent_context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        return {
            **super().get_context(value, parent_context),  # type: ignore
            "name": self.input_name,
        }


class AlertValue(StructValue):
    """`StructValue` for `AlertBlock`"""

    def get_icon(self, level: Optional[AlertLevel]) -> AlertIcon:
        """
        Get alert icon based on alert level.

        Args:
            level (str): Alert level

        Returns:
            str: Alert icon
        """

        match level:
            case "info":
                return level

            case "success":
                return "circle-check"

            case "warning":
                return "alert-triangle"

            case "error":
                return "x-circle"

            case _:
                return "question-mark-circle"

    @property
    def icon(self) -> str:
        """
        Get `AlertBlock` icon.

        Returns:
            str: Icon.
        """

        return self.get_icon(self.get("level"))


class CarouselValue(StructValue):
    """`StructValue` for `CarouselBlock`"""

    @property
    def item_count(self) -> int:
        """
        Get the number of items in `CarouselBlock`.

        Returns:
            int: Carousel items count.
        """

        return len(self.get("items", []))


class DocumentValue(StructValue):
    """`StructValue` for `DocumentBlock`"""

    def get_doc_size(self, size_bytes: int) -> str:
        """
        Converts a file size in bytes into a human-readable string (e.g., "1.43 MB").

        This method uses the binary prefix system (base 1024) and scales the
        unit dynamically based on the magnitude of the file size.

        Args:
            size_bytes (int): The total size of the document in bytes.

        Returns:
            str: A formatted string containing the scaled size and its unit.
        """

        if size_bytes <= 0:
            return "0 B"

        # Define the sequence of data units supported
        DATA_UNITS = ("B", "KB", "MB", "GB", "TB", "PB", "EB")

        # Determine the power of 1024 to which the size corresponds
        # log(size, 1024) returns the index of the unit in our DATA_UNITS tuple
        unit_index = int(math.floor(math.log(size_bytes, 1024)))

        # Safety check: ensure the index does not exceed our defined units
        unit_index = min(unit_index, len(DATA_UNITS) - 1)

        # Calculate the divisor: 1024 raised to the power of the unit index
        divisor = math.pow(1024, unit_index)

        # Scale the size and round to two decimal places for UI clarity
        scaled_size = round(size_bytes / divisor, 2)
        unit_label = DATA_UNITS[unit_index]

        return f"{scaled_size} {unit_label}"

    @property
    def doc_size(self) -> str:
        """
        Calculate and return the size of document in a human-readable format.

        Returns:
            size: Human-readable document size.
        """

        doc = self.get("document")
        return self.get_doc_size(doc.file_size if doc else 0)


class AttributeValue(StructValue):
    """Add an `self.attributes` to Value class"""

    prefix: str = ""
    exclude: List[str] = ["self"]

    @property
    def attributes(self) -> str:
        """
        Get HTML attributes the embed.

        Returns:
            size: HTML attributes to be used in the template.
        """

        return " ".join(
            [
                f"data-{self.prefix}{str(attribute).replace('_', '-')}={str(value)}"
                for attribute, value in self.items()
                if attribute not in self.exclude and value
            ]
        )


class CodePenValue(AttributeValue):
    """`StructValue` for `CodePenBlock`"""


class ExpoSnackValue(AttributeValue):
    """`StructValue` for `ExpoSnackBlock`"""

    prefix = "snack-"


class StackBlitzValue(StructValue):
    """`StructValue` for `StackBlitzBlock`"""

    exclude = ["self", "title", "url"]

    @property
    def params(self) -> str:
        """
        Get URL parameters.

        Returns:
            size: URL parameters to be used in the template.
        """

        return urlencode(
            {
                str(k).replace("_", "-"): v
                for k, v in self.items()
                if k not in self.exclude and v
            }
        )
