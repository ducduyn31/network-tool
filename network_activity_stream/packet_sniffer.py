from typing import Set

from network_activity_stream.shared_state import network_activity_state, packet_queue


def sniff_callback_builder(source_ips: Set[str]):
    def callback(packet):
        packet_size = len(packet)

        # Update the shared state
        packet_queue.put(packet)
        if packet.haslayer("IP"):
            ip_layer = packet["IP"]

            # Check if the packet is sent or received
            if ip_layer.src in source_ips:
                network_activity_state.last_second_sent_size += packet_size
            elif ip_layer.dst in source_ips:
                network_activity_state.last_second_received_size += packet_size

    return callback
