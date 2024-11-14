def get_total_profits(dataframe_dict):
    transactions_df = dataframe_dict["transactions"]

    total_profit = transactions_df.loc[transactions_df['total_price'] > 0, 'total_price'].sum()

    print(f"Total profits: {total_profit}")

"""
SQL Query:
    SELECT SUM(total_price) AS total_profits
    FROM transactions
    WHERE total_price > 0;
"""