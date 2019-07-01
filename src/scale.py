import pandas


class ScaleHandler:

    def __init__(self, csv_path="./scale.csv"):
        self.df = pandas.read_csv(csv_path)  # dataframe

    def get_freq(self, scalename):
        """
        scalename can be "A0" to "C8", use "#" not "b".
        """
        return self.df[self.df.name == scalename].freq
