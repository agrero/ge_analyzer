import pandas as pd
from python.Reader import Reader


class Converter(Reader):
    """
    A class that inherits from Reader and has latest_data and mapping_data attributes.
    """
    def __init__(self, file_path):
        """
        Initializes the Converter object with the file path and calls the Reader constructor.
        """
        super().__init__(file_path)
        
    def latest_data_to_dataframe(self):
        """
        Converts the latest_data attribute to a pandas dataframe.
        """
        
        latest_dataframe = pd.DataFrame(self.latest_data)

        # rename the columns
        #new_cols = [self.mapping_data[col] for col in latest_dataframe.columns]
        drop_cols = [col for col in latest_dataframe.columns if col not in self.mapping_data.keys()]

        return latest_dataframe.drop(drop_cols, axis=1)
    
