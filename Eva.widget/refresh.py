
import subprocess
import re

class GetSysInfo():
    def __init__(self):
        self.fetch_cpu_and_mem_usage()
        self.fetch_memory_pressure_level()
        self.fetch_cpu_cores()

    def fetch_cpu_and_mem_usage(self):
        try:
            # Run 'ps -A -o %cpu' to get CPU usage for all processes
            result = subprocess.run(['ps', '-A', '-o', '%cpu'], capture_output=True, text=True, check=True)
            output = result.stdout.strip().splitlines()

            # Sum up the CPU usage values (skip the header line if present)
            total_cpu_usage = sum(float(line) for line in output[1:] if line.strip())
            print(f"Total CPU Usage: {total_cpu_usage:.2f}%")
        except subprocess.CalledProcessError as e:
            print(f"Error fetching CPU usage: {e}")
            return

    def fetch_memory_pressure_level(self):
        try:
            # Run 'sysctl -a kern.memorystatus_vm_pressure_level' to get memory pressure level
            result = subprocess.run(['sysctl', '-a', 'kern.memorystatus_vm_pressure_level'], capture_output=True, text=True, check=True)
            output = result.stdout.strip()

            # Extract the second field (memory pressure level) using regular expression
            match = re.search(r'kern\.memorystatus_vm_pressure_level: (\d+)', output)
            if match:
                memory_pressure_level = int(match.group(1))
                print(f"Memory Pressure Level: {memory_pressure_level}")
            else:
                print("Memory pressure level not found.")
        except subprocess.CalledProcessError as e:
            print(f"Error fetching memory pressure level: {e}")
            return

    def fetch_cpu_cores(self):
        try:
            # Run 'sysctl hw.ncpu' to get the number of CPU cores
            result = subprocess.run(['sysctl', 'hw.ncpu'], capture_output=True, text=True, check=True)
            output = result.stdout.strip()

            # Extract the second field (number of CPU cores) using regular expression
            match = re.search(r'hw\.ncpu: (\d+)', output)
            if match:
                cpu_cores = int(match.group(1))
                print(f"Number of CPU Cores: {cpu_cores}")
            else:
                print("Number of CPU cores not found.")
        except subprocess.CalledProcessError as e:
            print(f"Error fetching number of CPU cores: {e}")
            return

class GetBattInfo():

    def __init__(self):
        try:
            result = subprocess.run(['pmset', '-g', 'batt'], capture_output=True, text=True, check=True)     # Get battery information via pmset
            output = result.stdout
        except subprocess.CalledProcessError as e:
            print(f"Error executing pmset command: {e}")
            return
        else:
            try:
                battery_info = next(line for line in output.splitlines() if '%' in line) # Split at battery percentage
            except StopIteration:
                print("No battery information found.")
                return

        fields = [field.strip() for field in battery_info.split(';') if field.strip()] # Split by semicolon, strip leading/trailing whitespace

        # Modify specific patterns: replace '-I' with 'I', remove '-0', and remove semicolons
        modified_fields = [
            re.sub(r'-I', 'I', field)  # Replace '-I' with 'I'
            .replace('-0', '')         # Remove '-0'
            .replace(';', '')          # Remove semicolons
            for field in fields
        ]

        # Print the modified fields
        print(" ".join(modified_fields))

# if __name__ == "__main__":
#     fetch_cpu_usage()
#     fetch_memory_pressure_level()
#     fetch_cpu_cores()
#     fetch_battery_info()

