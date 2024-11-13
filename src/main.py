from src.main_helpers.main_helpers import get_input_output_folders, print_df_info_to_console, get_dataframes, \
    create_data_profiles


def main():
    input_folder, output_folder = get_input_output_folders()
    dataframes = get_dataframes(input_folder=input_folder)
    dataframe_dict = {
        "customer": dataframes[0],
        "product": dataframes[1],
        "transactions": dataframes[2]
    }
    print_df_info_to_console(dataframe_dict=dataframe_dict)

    create_data_profiles(dataframe_dict=dataframe_dict, base_output_folder=output_folder)


if __name__ == "__main__":
    main()
