from abc import ABC, abstractmethod
from typing import Any, Tuple, List


class DataProcessor(ABC):
    """Abstract base class for data processors."""

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Process input data."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate input data."""
        pass

    @abstractmethod
    def format_output(self, result: Any) -> str:
        """Format processed result."""
        pass


class NumericProcessor(DataProcessor):
    """Processor for numeric data."""

    def process(self, data: List[float]) -> Tuple[int, int, float]:
        total = sum(data)
        count = len(data)
        avg = total / count
        return total, count, avg

    def validate(self, data: List[float]) -> bool:
        try:
            print("Initializing Numeric Processor...")
            print(f"Processing data: {data}")
            for element in data:
                float(element)
            print("Validation: Numeric data verified")
            return True
        except Exception:
            return False

    def format_output(
        self,
        result: Tuple[int, int, float],
    ) -> str:
        total, count, avg = result
        return (
            f"Processed {count} numeric values, "
            f"sum={total}, avg={avg}"
        )


class TextProcessor(DataProcessor):
    """Processor for text data."""

    def process(self, data: str) -> Tuple[int, int]:
        len_carac = len(data)
        len_words = len(data.split())
        return len_carac, len_words

    def validate(self, data: str) -> bool:
        try:
            print("Initializing Text Processor...")
            print(f'Processing data: "{data}"')
            print("Validation: Text data verified")
            return True
        except Exception:
            return False

    def format_output(
        self,
        result: Tuple[int, int],
    ) -> str:
        chars, words = result
        return (
            f"Processed text: {chars} characters, "
            f"{words} words"
        )


class LogProcessor(DataProcessor):
    """Processor for log entries."""

    def process(self, data: str) -> Tuple[str, str]:
        level, message = data.split(": ", 1)
        return level, message

    def validate(self, data: str) -> bool:
        try:
            print("Initializing Log Processor...")
            print(f'Processing data: "{data}"')
            print("Validation: Log entry verified")
            return True
        except Exception:
            return False

    def format_output(
        self,
        result: Tuple[str, str],
    ) -> str:
        level, message = result
        if level == "ERROR":
            return (
                f"[ALERT] {level} level detected: "
                f"{message}"
            )
        return (
            f"[INFO] {level} level detected: "
            f"{message}"
        )


if __name__ == "__main__":
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    n_proc = NumericProcessor()
    d_num = [1, 2, 3, 4, 5]

    if n_proc.validate(d_num):
        resultado = n_proc.process(d_num)
    print(f"Output: {n_proc.format_output(resultado)}\n")

    t_proc = TextProcessor()
    d_text = "Hello Nexus World"

    if t_proc.validate(d_text):
        resultado = t_proc.process(d_text)
    print(f"Output: {t_proc.format_output(resultado)}\n")

    l_proc = LogProcessor()
    d_log = "ERROR: Connection timeout"

    if l_proc.validate(d_log):
        resultado = l_proc.process(d_log)
    print(f"Output: {l_proc.format_output(resultado)}\n")

    print("=== Polymorphic Processing Demo ===")
    print(
        "Processing multiple data types "
        "through same interface...\n"
    )

    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    dates = [
        [1, 2, 3],
        "Hello World",
        "INFO: System ready",
    ]

    for i in range(len(processors)):
        p = processors[i]
        d = dates[i]

        result = p.process(d)
        out = p.format_output(result)
        print(f"Result {i + 1}: {out}")

    print(
        "\nFoundation systems online. "
        "Nexus ready for advanced streams."
    )
