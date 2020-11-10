from sqlalchemy import create_engine
from db_layer import models
import pandas as pd
import json
import os

class SqlCaller():
    """
    SqlCaller() --> This module is meant to dump various data into a database.
    Must instantiate SqlCaller() with census api key and db connection string

    Parameters:
    engine_string: define db connection here
    api_key: define api_key for census data. You can go to www.census.gov.
    """

    def __init__(self, create_tables=False):
        path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'un_pw.json'))

        with open(path, "r") as file:
            mysql_engine = json.load(file)['aws_mysql']
        engine_string = mysql_engine
        self.engine = create_engine(engine_string)

        if create_tables == True:
            print("Creating tables")
            models.InitiateDeclaratives.create_tables(engine_string)


    def db_get_Zillow_MSAID_Lookup(self):
        msa_ids = pd.read_sql_query("""select Geo_ID, Zillow_Id from Zillow_MSAID_Lookup""", self.engine)
        return msa_ids

    def db_dump_Zillow_MedianHomePrice(self, df):
        df.to_sql("Zillow_MedianHomePrice", if_exists='replace', con=self.engine, index=False)


    def db_dump_Zillow_MSAID_Lookup(self, df):
        df.to_sql("Zillow_MSAID_Lookup", if_exists='replace', con=self.engine, index=False)

    # def db_dump_Zillow_County_MedianHomePrice(self, df):
    #     df.to_sql("Zillow_County_MedianHomePrice", if_exists='replace', con=self.engine, index=False)
    #
    # def db_dump_Zillow_Zipcode_MedianHomePrice(self, df):
    #     df.to_sql("Zillow_Zipcode_MedianHomePrice", if_exists='replace', con=self.engine, index=False)

