import os
import json


class Reader:
    """
    A class that reads data from JSON files.
    """
    def __init__(self, file_path):
        """
        Initializes the Reader class.
        """
        # set the data directory and file paths
        self.data_dir = os.path.join(os.getcwd(), 'data')
        self.latest_file = os.path.join(self.data_dir, 'latest.json')
        self.mapping_file = os.path.join(self.data_dir, 'mapping.json')

        # initialize the data variables
        self.latest_data = None
        self.mapping_data = None
        
    def load_latest_data(self):
        """
        Loads the latest data from the latest.json file.
        """
        # open the latest.json file and load the data
        with open(self.latest_file, 'r') as f:
            self.latest_data = json.load(f)
        
    def load_mapping_data(self):
        """
        Loads the mapping data from the mapping.json file.
        """
        # open the mapping.json file and load the data
        with open(self.mapping_file, 'r') as f:
            self.mapping_data = json.load(f)
