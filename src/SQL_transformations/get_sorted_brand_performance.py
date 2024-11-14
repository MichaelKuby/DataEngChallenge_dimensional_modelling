def get_brand_performance(dataframe_dict):
    transactions_df = dataframe_dict['transactions']
    product_df = dataframe_dict['product']

    joined_df = transactions_df.merge(
        product_df,
        left_on='product_id',
        right_on='id',
        how='inner',
        suffixes=('_trans', '_prod')
    )

    brand_performance_df = joined_df.groupby('brand')['total_price'].sum().reset_index()
    brand_performance_df = brand_performance_df.rename(columns={'total_price': 'total_profit'})
    brand_performance_df = brand_performance_df.sort_values(by='total_profit', ascending=False).reset_index()

    top_brand = brand_performance_df.iloc[0]['brand']
    top_brand_profit = brand_performance_df.iloc[0]['total_profit']

    print("The top brand is: ", top_brand, " with a total profit of: ", top_brand_profit)

"""
SQL Query:
    SELECT brand, SUM(total_price) AS top_brand
    FROM transactions t
    INNER JOIN product p
    ON t.product_id = p.id
    GROUP BY brand
    ORDER BY total_profit DESC
    LIMIT 1;
"""