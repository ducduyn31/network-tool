import time

from network_activity_stream.shared_state import network_activity_state
from network_activity_stream.utils import format_mb

last_second_received_size = 0
last_second_sent_size = 0
last_report_time = time.time()


def periodic_report():
    """
    Periodically report the network activity (received and sent sizes) every second.
    """
    global last_second_received_size, last_second_sent_size, last_report_time

    while True:
        time.sleep(1)  # Wait for 1 second
        current_time = time.time()
        time_from = time.strftime("%H:%M:%S", time.localtime(network_activity_state.last_report_time))
        time_to = time.strftime("%H:%M:%S", time.localtime(current_time))

        received_mb = format_mb(network_activity_state.last_second_received_size)
        sent_mb = format_mb(network_activity_state.last_second_sent_size)
        total_mb = format_mb(
            network_activity_state.last_second_received_size + network_activity_state.last_second_sent_size)

        print(f"{time_from} to {time_to}: {received_mb} received, {sent_mb} sent, {total_mb} total")

        # Reset for the next second
        network_activity_state.last_second_received_size = 0
        network_activity_state.last_second_sent_size = 0
        network_activity_state.last_report_time = current_time
