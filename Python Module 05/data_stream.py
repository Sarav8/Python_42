from abc import ABC, abstractmethod
from typing import Any, List, Dict, Tuple


class DataStream(ABC):
    """Abstract base class for all data streams."""

    def __init__(self, stream_id: str, stream_type: str):
        self.stream_id = stream_id
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, data: Any) -> Any:
        """Process a batch of incoming data."""
        pass

    @abstractmethod
    def filter_data(self, data: Any) -> Any:
        """Filter invalid or irrelevant data."""
        pass

    @abstractmethod
    def get_stats(self, result: Any) -> str:
        """Return a summary of results."""
        pass


class SensorStream(DataStream):
    """Stream specialized in environmental sensor data."""

    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Environmental Data")
        self.readings: List[Any] = []

    def process_batch(self, data: Any) -> Any:
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")
        print(f"Processing sensor batch: {data}")
        filtered = self.filter_data(data)
        return self._process_internal(filtered)

    def filter_data(self, data: Any) -> Any:
        try:
            return [
                d for d in data
                if "temp" in d and isinstance(d["temp"], (int, float))
            ]
        except Exception as e:
            print(f"SensorStream filter error: {e}")
            return []

    def _process_internal(
        self,
        data: List[Dict[str, Any]]
    ) -> Tuple[int, float]:
        try:
            count = len(data)
            temps = [reading["temp"] for reading in data]
            avg = sum(temps) / len(temps) if temps else 0.0
            return count, avg
        except (KeyError, TypeError, ZeroDivisionError) as e:
            print(f"SensorStream error: {e}")
            return 0, 0.0

    def get_stats(self, result: Any) -> str:
        count, avg = result
        return (
            f"Sensor analysis: {count} readings processed, "
            f"avg temp: {avg}°C"
        )


class TransactionStream(DataStream):
    """Stream specialized in financial transaction data."""

    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Financial Data")
        self.operations: List[Any] = []

    def process_batch(self, data: Any) -> Any:
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")
        print(f"Processing transaction batch: {data}")
        filtered = self.filter_data(data)
        return self._process_internal(filtered)

    def filter_data(self, data: Any) -> Any:
        try:
            return [
                d for d in data
                if "type" in d and "amount" in d and d["amount"] != 0
            ]
        except Exception as e:
            print(f"TransactionStream filter error: {e}")
            return []

    def _process_internal(self, data: Any) -> Any:
        try:
            net_flow = 0
            for oper in data:
                if oper["type"] == "buy":
                    net_flow += oper["amount"]
                elif oper["type"] == "sell":
                    net_flow -= oper["amount"]
            count = len(data)
            return count, net_flow
        except KeyError as e:
            print(f"TransactionStream error: missing key {e}")
            return 0, 0.0
        except TypeError as e:
            print(f"TransactionStream error: wrong data type {e}")
            return 0, 0.0
        except ZeroDivisionError:
            print("TransactionStream error: no data to process")
            return 0, 0.0

    def get_stats(self, result: Any) -> str:
        count, net_flow = result
        return (
            f"Transaction analysis: {count} operations, "
            f"net flow: +{net_flow} units"
        )


class EventStream(DataStream):
    """Stream specialized in system event data."""

    def __init__(self, stream_id: str):
        super().__init__(stream_id, "System Events")
        self.events: List[Any] = []

    def process_batch(self, data: Any) -> Any:
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")
        print(f"Processing event batch: {data}")
        filtered = self.filter_data(data)
        return self._process_internal(filtered)

    def filter_data(self, data: Any) -> Any:
        try:
            valid_types = {"login", "logout", "error"}
            return [
                d for d in data
                if "type" in d and d["type"] in valid_types
            ]
        except Exception as e:
            print(f"EventStream filter error: {e}")
            return []

    def _process_internal(self, data: Any) -> Any:
        try:
            count_error = 0
            count_login = 0
            count_logout = 0
            for event in data:
                if event["type"] == "error":
                    count_error += 1
                elif event["type"] == "login":
                    count_login += 1
                elif event["type"] == "logout":
                    count_logout += 1
            count = len(data)
            return count, count_logout, count_error, count_login
        except TypeError as e:
            print(f"EventStream error: {e}")
            return 0, 0, 0, 0

    def get_stats(self, result: Any) -> str:
        count, _, count_error, _ = result
        return (
            f"Event analysis: {count} events, "
            f"{count_error} error detected"
        )


class StreamProcessor:
    """Coordinates processing across multiple stream types."""

    def __init__(self, data_streams: List[DataStream]):
        self.streams: List[DataStream] = data_streams

    def process_stream(self) -> None:
        print("\nBatch 1 Results:")

        filtered_results = {
            "Sensor": 0,
            "Transaction": 0,
            "Event": 0
        }

        for stream in self.streams:
            if isinstance(stream, SensorStream):
                data = [
                    {"temp": 30, "humidity": 65},
                    {"temp": 28, "pressure": 1013}
                ]
            elif isinstance(stream, TransactionStream):
                data = [
                    {"type": "buy", "amount": 200},
                    {"type": "sell", "amount": 150},
                    {"type": "buy", "amount": 100},
                    {"type": "sell", "amount": 50}
                ]
            elif isinstance(stream, EventStream):
                data = [
                    {"type": "login"},
                    {"type": "error"},
                    {"type": "logout"}
                ]
            else:
                continue

            filtered = stream.filter_data(data)
            results = stream._process_internal(filtered)

            if isinstance(stream, SensorStream):
                count, avg_temp = results
                print(f"- Sensor data: {count} readings processed")
                if avg_temp > 25:
                    filtered_results["Sensor"] += count

            elif isinstance(stream, TransactionStream):
                count, net_flow = results
                print(f"- Transaction data: {count} operations processed")
                if net_flow > 100:
                    filtered_results["Transaction"] += 1

            elif isinstance(stream, EventStream):
                count, _, count_error, _ = results
                print(f"- Event data: {count} events processed")
                filtered_results["Event"] += count_error

        print("\nStream filtering active: High-priority data only")
        print(
            f"Filtered results: {filtered_results['Sensor']} "
            f"critical sensor alerts, "
            f"{filtered_results['Transaction']} large transaction"
        )
        print(
            "\nAll streams processed successfully. "
            "Nexus throughput optimal."
        )


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    p_sensor = SensorStream("SENSOR_001")
    d_sensor = [{"temp": 22.5, "humidity": 65, "pressure": 1013}]
    result = p_sensor.process_batch(d_sensor)
    analysis = p_sensor.get_stats(result)
    print(f"{analysis}\n")

    p_oper = TransactionStream("TRANS_001")
    d_oper = [
        {"type": "buy", "amount": 100},
        {"type": "sell", "amount": 150},
        {"type": "buy", "amount": 75}
    ]
    result = p_oper.process_batch(d_oper)
    analysis = p_oper.get_stats(result)
    print(f"{analysis}\n")

    p_event = EventStream("EVENT_001")
    d_event = [
        {"type": "login"},
        {"type": "error"},
        {"type": "logout"}
    ]
    result = p_event.process_batch(d_event)
    analysis = p_event.get_stats(result)
    print(f"{analysis}\n")

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    streams = [
        SensorStream("SENSOR_001"),
        TransactionStream("TRANS_001"),
        EventStream("EVENT_001")
    ]

    processor = StreamProcessor(streams)
    processor.process_stream()
