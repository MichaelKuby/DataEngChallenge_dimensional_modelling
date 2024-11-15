def convert_customer_id_to_int(dataframe_dict):
    transactions_df = dataframe_dict["transactions"]
    transactions_df["customer_id"] = (
        transactions_df["customer_id"].fillna(-1).astype(int)
    )
    dataframe_dict["transactions"] = transactions_df


def pre_processing(dataframe_dict):
    convert_customer_id_to_int(dataframe_dict)
