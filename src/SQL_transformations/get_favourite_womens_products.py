def get_favourite_womens_product_df(dataframe_dict):
    transactions_df = dataframe_dict['transactions']
    product_df = dataframe_dict['product']
    customer_df = dataframe_dict['customer']

    joined_trans_and_prod_df = transactions_df.merge(
        product_df,
        left_on='product_id',
        right_on='id',
        how='inner',
        suffixes=('_trans', '_prod')
    )

    female_customers = customer_df[customer_df['gender'] == 'Female']
    female_customers = female_customers.rename(columns={'id': 'female_customer_id'})

    joined = joined_trans_and_prod_df.merge(
        female_customers,
        left_on='customer_id',
        right_on='female_customer_id',
        how='inner',
        suffixes=('_joined', '_female_cust')
    )

    favourite_womens_product = joined['product_id'].value_counts()
    favourite_womens_products = favourite_womens_product[favourite_womens_product == favourite_womens_product.max()]

    return favourite_womens_product, favourite_womens_products