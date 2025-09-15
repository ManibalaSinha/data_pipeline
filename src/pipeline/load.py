def load_to_db(df, conn, table_name="transactions"):
    df.to_sql(table_name, conn, if_exists='replace', index=False)
