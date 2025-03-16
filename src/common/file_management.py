import pandas as pd


def read_currency_dataset(currency: str, price_side: str) -> dict:
    """
    Read the currency dataset from the csv file and return it as a dictionary.
    :param currency: str
    :param price_side: str
    :return: dict
    """
    # Read the dataset from the csv file
    dataset = pd.read_csv(f'../data/{currency}_{price_side}.csv')
    # Convert the dataset to a dictionary
    dataset_dict = dataset.to_dict(orient='records')
    return dataset_dict
