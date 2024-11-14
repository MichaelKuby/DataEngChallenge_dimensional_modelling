def sort_customers_by_importance(dataframe_dict):
    customer_df = dataframe_dict['customer']
    transactions_df = dataframe_dict['transactions']

    joined_df = transactions_df.merge(
        customer_df,
        left_on='customer_id',
        right_on='id',
        how='inner',
        suffixes=('_trans', '_cust')
    )

    customer_value_df = joined_df.groupby('customer_id')['total_price'].sum().reset_index()
    customer_value_df = customer_value_df.rename(columns={'total_price': 'total_value'})
    customer_value_df = customer_value_df.sort_values(by='total_value', ascending=False).reset_index().drop('index', axis=1)

    print(customer_value_df)

"""
SQL Query:
    SELECT t.customer_id, SUM(t.total_price) AS total_value
    FROM transactions t
    INNER JOIN customer c
    ON t.customer_id = c.id
    GROUP BY t.customer_id
    ORDER BY total_value DESC;
"""