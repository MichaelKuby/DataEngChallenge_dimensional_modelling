import os
import pandas as pd

from pandas_profiling import ProfileReport


def get_input_output_folders():
    base_folder = os.path.dirname(os.path.abspath(__file__ + "/../.."))
    data_folder = os.path.join(base_folder, 'data')
    input_folder = os.path.join(data_folder, 'input')
    output_folder = os.path.join(data_folder, 'output')
    return input_folder, output_folder


def get_customer_data(input_folder, filename):
    file_path = os.path.join(input_folder, filename)
    df = pd.read_csv(file_path)
    return df


def get_product_data(input_folder, filename):
    file_path = f"{input_folder}/{filename}"

    try:
        df = pd.read_xml(file_path)
        return df
    except Exception as e:
        print(f"An error occurred while reading the XML file: {e}")
        return None


def get_transactions_data(input_folder, filename):
    file_path = os.path.join(input_folder, filename)

    try:
        df = pd.read_json(file_path)
        return df
    except Exception as e:
        print(f"An error occurred while reading the JSON file: {e}")
        return None


def get_dataframes(input_folder):
    customer_df = get_customer_data(input_folder=input_folder, filename='customer_data.csv')
    product_df = get_product_data(input_folder=input_folder, filename='products.xml')
    transactions_df = get_transactions_data(input_folder=input_folder, filename='transactions.json')
    return [customer_df, product_df, transactions_df]


def print_df_info_to_console(dataframe_dict):
    for key, df in dataframe_dict.items():
        print(f"Dataframe: {key}")
        print(df.info())
        print(df.head())
        print("\n")


def create_data_profiles(dataframe_dict, base_output_folder):
    for name, df in dataframe_dict.items():
        profile = ProfileReport(df)
        profiles_folder = os.path.join(base_output_folder, 'profiles')
        os.makedirs(profiles_folder, exist_ok=True)
        profile_filename = os.path.join(profiles_folder, f"{name}_profile.html")
        profile.to_file(profile_filename)
        print(f"Profile for dataframe {name} created at: {profile_filename}")
