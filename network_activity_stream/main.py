import argparse
import threading

from scapy.all import sniff

from network_activity_stream.packet_sniffer import sniff_callback_builder
from network_activity_stream.utils import select_network_interfaces
from network_activity_stream.workers.pcap_writer import write_to_file_worker
from network_activity_stream.workers.reporter import periodic_report


def parse_arguments():
    parser = argparse.ArgumentParser(description="Network activity capture tool")
    parser.add_argument(
        "-i", "--interfaces",
        type=str,
        nargs='+',
        help="List of network interfaces to monitor. If not provided, the default interfaces will be used."
    )
    return parser.parse_args()


def start_workers():
    """
    Start the worker threads for writing packets to file and reporting network activity.

    This function initializes and starts two daemon threads:
    1. write_worker_thread: Responsible for writing captured packets to files in chunks.
    2. size_report_thread: Responsible for periodically reporting the network activity (received and sent sizes).

    Both threads run indefinitely in the background as daemon threads.
    """

    write_worker_thread = threading.Thread(target=write_to_file_worker, daemon=True)
    write_worker_thread.start()

    size_report_thread = threading.Thread(target=periodic_report, daemon=True)
    size_report_thread.start()


def main():
    args = parse_arguments()

    start_workers()

    # Select network interfaces based on CLI input or defaults
    if args.interfaces:
        network_interfaces = select_network_interfaces(prefer_interfaces=args.interfaces)
    else:
        network_interfaces = select_network_interfaces()

    interfaces_names = list(network_interfaces.keys())
    local_ips = set()
    for name, addresses in network_interfaces.items():
        for address in addresses:
            local_ips.add(address.address)

    # Sniffing packets on all network interfaces
    print(f"Sniffing packets from {' '.join(interfaces_names)}...")
    sniff(iface=interfaces_names, prn=sniff_callback_builder(local_ips))


if __name__ == "__main__":
    main()
