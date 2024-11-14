from src.SQL_transformations.get_favourite_mens_product import get_favourite_mens_product_df
from src.SQL_transformations.get_favourite_womens_products import get_favourite_womens_product_df


def get_products_men_and_women_love(dataframe_dict):
    _, favourite_mens_products = get_favourite_mens_product_df(dataframe_dict)
    _, favourite_womens_products = get_favourite_womens_product_df(dataframe_dict)

    # convert favourite_womens_products and favourite_mens_products to sets
    favourite_womens_products = set(favourite_womens_products.index.tolist())
    favourite_mens_products = set(favourite_mens_products.index.tolist())

    # find their intersection
    products = favourite_womens_products.intersection(favourite_mens_products)

    if len(products) == 0:
        print("There are no products that both men and women love.")
    else:
        print("The products that both men and women love are: ", products)