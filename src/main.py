from src.SQL_transformations.get_products_men_and_women_love import get_products_men_and_women_love
from src.SQL_transformations.get_sorted_brand_performance import get_brand_performance
from src.SQL_transformations.get_num_products_sold_w_profits import get_number_of_products_sold_with_profits_python
from src.SQL_transformations.get_total_profits import get_total_profits
from src.SQL_transformations.get_customers_sorted_by_importance import get_customers_sorted_by_importance
from src.main_helpers.main_helpers import get_input_output_folders, print_df_info_to_console, get_dataframes, \
    create_data_profiles
from src.pre_processing_steps.pre_processing import pre_processing
from src.SQL_transformations.get_favourite_mens_product import get_favourite_mens_product


def main():
    input_folder, output_folder = get_input_output_folders()
    dataframe_dict = get_dataframes(input_folder=input_folder)

    print_df_info_to_console(dataframe_dict=dataframe_dict)
    create_data_profiles(dataframe_dict=dataframe_dict, base_output_folder=output_folder)

    pre_processing(dataframe_dict=dataframe_dict)

    get_number_of_products_sold_with_profits_python(dataframe_dict=dataframe_dict)
    get_total_profits(dataframe_dict=dataframe_dict)
    get_brand_performance(dataframe_dict=dataframe_dict)
    get_customers_sorted_by_importance(dataframe_dict=dataframe_dict)
    get_favourite_mens_product(dataframe_dict=dataframe_dict)
    get_products_men_and_women_love(dataframe_dict=dataframe_dict)


if __name__ == "__main__":
    main()
