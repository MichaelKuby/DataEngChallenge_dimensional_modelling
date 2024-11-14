def get_number_of_products_sold_with_profits_python(dataframe_dict):
    transactions_df = dataframe_dict["transactions"]

    products_sold_with_profits = transactions_df[transactions_df['total_price'] > 0]

    num_products_sold_with_profits = products_sold_with_profits['product_id'].nunique()

    print(f"Number of products sold with profits: {num_products_sold_with_profits}")

"""
SQL Query:
    SELECT COUNT(DISTINCT product_id) AS num_products_sold_with_profits
    FROM transactions
    WHERE total_price > 0;
"""