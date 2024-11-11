import pandas as pd

class CSVStreamerPandas:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)  # Load the CSV into a DataFrame
        self.current_index = 0  # Initialize the current row index

    def get_next_row(self):
        # Check if there are rows left to return
        if self.current_index < len(self.data):
            row = self.data.iloc[self.current_index].to_dict()  # Get the current row
            self.current_index += 1  # Move to the next row
            return row
        else:
            # Return None if no more rows are available
            return None