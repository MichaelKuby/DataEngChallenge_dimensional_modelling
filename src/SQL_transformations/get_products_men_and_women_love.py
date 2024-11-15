from src.SQL_transformations.get_favourite_products import (
    get_favourite_product_by_gender,
)


def get_products_men_and_women_love(dataframe_dict):
    _, favourite_mens_products = get_favourite_product_by_gender(
        dataframe_dict=dataframe_dict, gender="Male"
    )
    _, favourite_womens_products = get_favourite_product_by_gender(
        dataframe_dict=dataframe_dict, gender="Female"
    )

    # convert favourite_womens_products and favourite_mens_products to sets and find their intersection
    favourite_womens_products = set(favourite_womens_products.index.tolist())
    print("favourite_womens_products:", favourite_womens_products)
    favourite_mens_products = set(favourite_mens_products.index.tolist())
    print("favourite_mens_products:", favourite_mens_products)
    products = favourite_womens_products.intersection(favourite_mens_products)

    if len(products) == 0:
        print(
            "There are no products that both men and women love based on the number of times purchased."
        )
    else:
        print("The products that both men and women love are: ", products)


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
FemaleCustomers AS (
    SELECT id AS female_customer_id
    FROM customer
    WHERE gender = 'Female'
),
MaleJoined AS (
    SELECT jtp.product_id
    FROM JoinedTransProd jtp
    INNER JOIN MaleCustomers mc ON jtp.customer_id = mc.male_customer_id
),
FemaleJoined AS (
    SELECT jtp.product_id
    FROM JoinedTransProd jtp
    INNER JOIN FemaleCustomers fc ON jtp.customer_id = fc.female_customer_id
),
MaleProductCount AS (
    SELECT product_id, COUNT(*) AS male_purchase_count
    FROM MaleJoined
    GROUP BY product_id
),
FemaleProductCount AS (
    SELECT product_id, COUNT(*) AS female_purchase_count
    FROM FemaleJoined
    GROUP BY product_id
),
MaxMalePurchaseCount AS (
    SELECT MAX(male_purchase_count) AS max_male_count
    FROM MaleProductCount
),
MaxFemalePurchaseCount AS (
    SELECT MAX(female_purchase_count) AS max_female_count
    FROM FemaleProductCount
),
TopMaleProducts AS (
    SELECT mpc.product_id, mpc.male_purchase_count
    FROM MaleProductCount mpc
    INNER JOIN MaxMalePurchaseCount mmc ON mpc.male_purchase_count = mmc.max_male_count
),
TopFemaleProducts AS (
    SELECT fpc.product_id, fpc.female_purchase_count
    FROM FemaleProductCount fpc
    INNER JOIN MaxFemalePurchaseCount mfc ON fpc.female_purchase_count = mfc.max_female_count
)
SELECT tmp.product_id, tmp.male_purchase_count, tfp.female_purchase_count
FROM TopMaleProducts tmp
INNER JOIN TopFemaleProducts tfp ON tmp.product_id = tfp.product_id;
"""
