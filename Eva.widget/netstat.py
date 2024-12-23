
import os
import subprocess
import threading
from queue import Queue
import time
import cmd

# Constants for the OpenDNS resolver and file paths (simulated in memory)
OPENDNS_RESOLVER = 'resolver1.opendns.com'
MYIP_QUERY = 'myip.opendns.com'
ROUTE_COMMAND = ['route', 'get', '-host', OPENDNS_RESOLVER]
NETSTREAM_COMMAND = ['netstat', '-w1', '-I']
ADDRESS_COMMAND = ['dig', '+short', 'myip.opendns.com', '+tries=5', '@resolver1.opendns.com']
NETSTAT_INTERVAL = 1
SLEEP_DURATION = 5

class RevealNetworkInterface:

    def reveal(self):
        """Get the network interface used to reach a specific host."""
        try:
            result = subprocess.run(ROUTE_COMMAND, capture_output=True, text=True, check=True)
            for line in result.stdout.splitlines():
                if 'interface' in line:
                    return line.split()[1]
            raise ValueError("Interface not found")
        except subprocess.CalledProcessError as e:
            print(f"Error getting network interface: {e}")
            return None


class ShowNetworkStream:

    def poll_with_netstat(self, interface_name, queue):
        """Run netstat and capture the output for a specific interface."""
        try:
            # Run netstat with a timeout
            command_with_interface = NETSTREAM_COMMAND
            command_with_interface.append(interface_name)
            netstat_process = subprocess.Popen(command_with_interface,  shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            sleep_thread = threading.Thread(target=lambda: (time.sleep(NETSTAT_INTERVAL), netstat_process.kill()))
            sleep_thread.start()

            # Capture the output
            output, _ = netstat_process.communicate()
            lines = output.decode('utf-8').splitlines()
            if len(lines) > 1:
                data = lines[2].split()
                if len(data) >= 5:
                    received = data[1]
                    send = data[2]
                    # nat_ip = data[4]
                    queue.put((received, send, interface_name))

        except subprocess.CalledProcessError as e:
            print(f"Error running netstat: {e}")
            queue.put(None)

class ShowIPAddress:
    def reflected_ip(self):
        """Get the external IP address using OpenDNS."""
        try:
            result = subprocess.run(ADDRESS_COMMAND, capture_output=True, text=True, check=True)
            ip_address = result.stdout.strip()
            if not self.__is_valid_ip(ip_address):
                return "Fehler"
            return ip_address
        except subprocess.CalledProcessError as e:
            print(f"Error getting external IP: {e}")
            return "Fehler"

    def __is_valid_ip(self,ip):
        """Check if the given string is a valid IPv4 address."""
        import re
        pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
        return bool(re.match(pattern, ip))

class StartQueue:
    def network_activity(self, queue):
        """Run the netstat data collection and put results in the queue."""
        interface = RevealNetworkInterface()
        interface_name = interface.reveal()
        if interface_name:
            transmissions = ShowNetworkStream()
            transmissions.poll_with_netstat(interface_name, queue)

    def wan_address(self, queue):
        """Get the external IP address and put it in the queue."""
        show = ShowIPAddress()
        ip_address = show.reflected_ip()
        queue.put(ip_address)

class RecordNetworkState():
    def __init__(self):

        # Queues to store results
        netstat_queue = Queue()
        ip_queue = Queue()

        # Run data collection and IP retrieval in separate threads
        retrieve = StartQueue()
        data_thread = threading.Thread(target=retrieve.network_activity, args=(netstat_queue,))
        ip_thread = threading.Thread(target=retrieve.wan_address, args=(ip_queue,))

        data_thread.start()
        ip_thread.start()

        # Wait for both threads to complete
        data_thread.join()
        ip_thread.join()

        # Collect results from queues
        netstat_result = netstat_queue.get() if not netstat_queue.empty() else None
        ip_result = ip_queue.get() if not ip_queue.empty() else "Fehler"

        # Format and print the output
        if netstat_result:
            output_line1 = f"{netstat_result[0]} {netstat_result[1]} {netstat_result[2]}"
        else:
            output_line1 = "Netstat failed"

        output_line2 = ip_result

        print(output_line1)
        print(output_line2)

if __name__ == "__main__":
    RecordNetworkState()
