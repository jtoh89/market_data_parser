import pandas as pd
import os
from sqlalchemy import create_engine
from db_layer import sql_caller

path = os.path.dirname(os.path.abspath(__file__))
path = path + '/zillowdata'


final_df = pd.DataFrame()

for filename in os.listdir(path):

    if 'Zip' in filename:
        df = pd.read_csv(path + '/' + filename)

        latest_date = df.columns[-1:][0]
        df = df[['RegionName', latest_date]].rename(columns={'RegionName':'Geo_ID',latest_date: 'MedianHomePrice'})

        df['Geo_Type'] = 'Zipcode'

        sql = sql_caller.SqlCaller(create_tables=True)
        sql.db_dump_Zillow_MedianHomePrice(df)



    # if 'County' in filename:
    #     df = pd.read_csv(path + '/' + filename)
    #
    #     latest_date = df.columns[-1:][0]
    #     df = df[['RegionName','State','Metro','StateCodeFIPS','MunicipalCodeFIPS',latest_date]].rename(columns={latest_date:'MedianHomePrice'})
    #
    #     df['StateCodeFIPS'] = df['StateCodeFIPS'].astype(str).str.zfill(2)
    #     df['MunicipalCodeFIPS'] = df['MunicipalCodeFIPS'].astype(str).str.zfill(3)
    #
    #     df['Geo_ID'] = df['StateCodeFIPS'] + df['MunicipalCodeFIPS']
    #     df['Geo_Type'] = 'County'
    #
    #     df = df.drop(columns=['State','Metro','StateCodeFIPS','MunicipalCodeFIPS'])
    #
    #     sql = sql_caller.SqlCaller(create_tables=True)
    #     sql.db_dump_Zillow_County_MedianHomePrice(df)




