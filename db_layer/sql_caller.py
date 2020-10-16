from sqlalchemy import create_engine
from db_layer import models
import pandas as pd
import json

class SqlCaller():
    """
    SqlCaller() --> This module is meant to dump various data into a database.
    Must instantiate SqlCaller() with census api key and db connection string

    Parameters:
    engine_string: define db connection here
    api_key: define api_key for census data. You can go to www.census.gov.
    """

    def __init__(self, create_tables=False):
        with open("./un_pw.json", "r") as file:
            mysql_engine = json.load(file)['aws_mysql']
        engine_string = mysql_engine
        self.engine = create_engine(engine_string)

        if create_tables == True:
            print("Creating tables")
            models.InitiateDeclaratives.create_tables(engine_string)


    def db_dump_Zillow_MedianHomePrice(self, df):
        df.to_sql("Zillow_MedianHomePrice", if_exists='replace', con=self.engine, index=False)

    # def db_dump_Zillow_County_MedianHomePrice(self, df):
    #     df.to_sql("Zillow_County_MedianHomePrice", if_exists='replace', con=self.engine, index=False)
    #
    # def db_dump_Zillow_Zipcode_MedianHomePrice(self, df):
    #     df.to_sql("Zillow_Zipcode_MedianHomePrice", if_exists='replace', con=self.engine, index=False)

