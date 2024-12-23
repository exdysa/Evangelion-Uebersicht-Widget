
import os
import subprocess
import json

# Constants
VOLUMES_PATH = "/Volumes"
BACKUP_FILE = os.path.join(os.getcwd(),"volumes.json")

class SaveVolumes():

    def __init__(self):
        # List all volumes and write them to a backup file
        volumes = self.list_volumes()
        if volumes:
            self.write_volumes_to_file(volumes, BACKUP_FILE)

    def list_volumes(self) -> list:
        """List all volumes in the /Volumes directory."""
        try:
            volumes = os.listdir(VOLUMES_PATH)         # Use `os.listdir` to get a list of volume names
            volumes = [vol for vol in volumes if not vol.startswith('.')] # Filter out any system-related directories (optional)
            return volumes
        except FileNotFoundError:
            print(f"Error: {VOLUMES_PATH} not found.")
            return []
        except Exception as e:
            print(f"An error occurred while listing volumes: {e}")
            return []

    def write_volumes_to_file(self, volumes: list, file_path: str):
        """Write the list of volumes to a backup file in JSON format."""
        try:
            with open(file_path, 'w') as f:
                json.dump(volumes, f, indent=4)
            print(f"Volumes written to {file_path}")
        except IOError as e:
            print(f"Error writing to {file_path}: {e}")

class PopVolumes():
    def __init__(self, num):
            volumes = self.read_volumes_from_file(BACKUP_FILE)

            # Open the first volume in Finder
            if volumes:
                try:
                    self.open_volume(volumes[num])
                except KeyError as error:
                    print(f"{error} Missing volume data, operation ended prematurely.")
                    return
            else:
                print("No volumes found to open.")

    def read_volumes_from_file(self,file_path: str=BACKUP_FILE) -> list:
        """Read the list of volumes from a backup file in JSON format."""
        try:
            with open(file_path, 'r') as f:
                volumes = json.load(f)
            return volumes
        except FileNotFoundError:
            print(f"Error: {file_path} not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error: {file_path} is not a valid JSON file.")
            return []
        else:
            print("No volumes found.")

    def open_volume(self,volume_name):
        """Open the specified volume in macOS Finder."""
            # Optionally, read the volumes from the backup file for testing
        try:
            # Use `subprocess.run` to execute the `open` command with the volume path
            subprocess.run(['open', os.path.join(VOLUMES_PATH, volume_name)], check=True)
            print(f"Opened: {volume_name}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to open {volume_name}: {e}")


# if __name__ == "__main__":
#     instance = SaveVolumes()
#     instance = PopVolumes(0)
