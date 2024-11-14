def get_favourite_mens_product_df(dataframe_dict):
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

    male_customers = customer_df[customer_df['gender'] == 'Male']
    male_customers = male_customers.rename(columns={'id': 'male_customer_id'})

    joined = joined_trans_and_prod_df.merge(
        male_customers,
        left_on='customer_id',
        right_on='male_customer_id',
        how='inner',
        suffixes=('_joined', '_male_cust')
    )

    favourite_mens_product = joined['product_id'].value_counts()
    favourite_mens_products = favourite_mens_product[favourite_mens_product == favourite_mens_product.max()]

    return favourite_mens_product, favourite_mens_products


def get_favourite_mens_product(dataframe_dict):
    favourite_mens_product, favourite_mens_products = get_favourite_mens_product_df(dataframe_dict)

    favourite_mens_products = favourite_mens_products.index.tolist()
    number_of_times_purchased = favourite_mens_product.max()

    print("The favourite mens products have product_id's: ", favourite_mens_products,
          " and they have each been purchased ", number_of_times_purchased, " times.")


"""
SQL Query:
    WITH JoinedTransProd AS (
        SELECT t.product_id, t.customer_id
        FROM transactions t
        INNER JOIN product p ON t.product_id = p.id
    ),
    MaleCustomers AS (
        SELECT id AS male_customer_id
        FROM customer
        WHERE gender = 'Male'
    ),
    Joined AS (
        SELECT jtp.product_id
        FROM JoinedTransProd jtp
        INNER JOIN MaleCustomers mc ON jtp.customer_id = mc.male_customer_id
    ),
    ProductCount AS (
        SELECT product_id, COUNT(*) AS purchase_count
        FROM Joined
        GROUP BY product_id
    ),
    MaxPurchaseCount AS (
        SELECT MAX(purchase_count) AS max_count
        FROM ProductCount
    )
    SELECT pc.product_id, pc.purchase_count
    FROM ProductCount pc
    INNER JOIN MaxPurchaseCount mpc ON pc.purchase_count = mpc.max_count;
"""
