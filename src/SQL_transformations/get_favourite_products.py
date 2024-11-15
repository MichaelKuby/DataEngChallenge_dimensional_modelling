def get_favourite_product_by_gender(dataframe_dict, gender):
    transactions_df = dataframe_dict["transactions"]
    product_df = dataframe_dict["product"]
    customer_df = dataframe_dict["customer"]

    joined_trans_and_prod_df = transactions_df.merge(
        product_df,
        left_on="product_id",
        right_on="id",
        how="inner",
        suffixes=("_trans", "_prod"),
    )

    # Filter customers based on specified gender
    gender_customers = customer_df[customer_df["gender"] == gender]
    gender_customers = gender_customers.rename(columns={"id": "customer_id_by_gender"})

    joined = joined_trans_and_prod_df.merge(
        gender_customers,
        left_on="customer_id",
        right_on="customer_id_by_gender",
        how="inner",
        suffixes=("_joined", f"_{gender.lower()}_cust"),
    )

    favourite_product = joined["product_id"].value_counts()
    favourite_products = favourite_product[favourite_product == favourite_product.max()]

    return favourite_product, favourite_products


def get_favourite_product(dataframe_dict, gender):
    favourite_product, favourite_products = get_favourite_product_by_gender(
        dataframe_dict, gender
    )

    favourite_products = favourite_products.index.tolist()
    number_of_times_purchased = favourite_product.max()

    print(
        f"The favourite products for {gender.lower()}s have product_id's: ",
        favourite_products,
        f" and they have each been purchased {number_of_times_purchased} times.",
    )
