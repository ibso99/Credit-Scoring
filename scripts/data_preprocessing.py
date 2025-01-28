import pandas as pd

class DataPreprocessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.df = None

    def load_data(self):
        self.df = pd.read_csv(self.input_file)

    def drop_duplicates(self):
        self.df.drop_duplicates(inplace=True)

    def convert_to_datetime(self):
        self.df['TransactionStartTime'] = pd.to_datetime(self.df['TransactionStartTime'], errors='coerce')

    def handle_missing_values(self):
        self.df['TransactionStartTime'].fillna(self.df['TransactionStartTime'].mode()[0], inplace=True)

    def save_cleaned_data(self):
        self.df.to_csv(self.output_file, index=False)

    def summarize_data(self):
        print("/nCleaned Data Info:")
        print(self.df.info())

    def preprocess(self):
        self.load_data()
        self.drop_duplicates()
        self.convert_to_datetime()
        self.handle_missing_values()
        self.summarize_data()
        self.save_cleaned_data()


if __name__ == "__main__":
    input_file = 'C:/Users/ibsan/Desktop/TenX/week-6/Data/data.csv'
    output_file = 'C:/Users/ibsan/Desktop/TenX/week-6/Data/cleaned_data.csv'
    preprocessor = DataPreprocessor(input_file, output_file)
    preprocessor.preprocess()