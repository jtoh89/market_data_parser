import pandas as pd
import os
from sqlalchemy import create_engine
from db_layer import sql_caller
import sys


path = os.path.dirname(os.path.abspath(__file__))
path = path + '/zillowdata'


final_df = pd.DataFrame()

for filename in os.listdir(path):

    if 'Metro' in filename:
        df = pd.read_csv(path + '/' + filename)

        print('Metro has {}'.format(len(df)))

        latest_date = df.columns[-1:][0]
        df = df[['RegionID','RegionName', latest_date]].rename(columns={'RegionID':'Zillow_Id',latest_date: 'MedianHomePrice'})
        df['Zillow_Id'] = df['Zillow_Id'].astype(str)
        sql = sql_caller.SqlCaller(create_tables=False)
        msaid_lookup = sql.db_get_Zillow_MSAID_Lookup()

        common = df.merge(msaid_lookup, on=['Zillow_Id', 'Zillow_Id'])

        missing = df[(~df.Zillow_Id.isin(common.Zillow_Id))]

        if len(missing) > 2:
            print('!!!! Missing more Zillow MSA !!!!')
            sys.exit()

        common['Geo_Type'] = 'Metro'
        common = common.drop(columns=['Zillow_Id'])
        if final_df.empty:
            final_df = common
        else:
            final_df = final_df.append(common)


    if 'Zip' in filename:
        df = pd.read_csv(path + '/' + filename)
        df['RegionName'] = df['RegionName'].astype(str).str.zfill(5)
        print('Zip has {}'.format(len(df)))

        latest_date = df.columns[-1:][0]

        df = df[['RegionName', latest_date]].rename(columns={'RegionName':'Geo_ID',latest_date: 'MedianHomePrice'})
        df['RegionName'] = df['Geo_ID']
        df['Geo_Type'] = 'Zipcode'

        if final_df.empty:
            final_df = df
        else:
            final_df = final_df.append(df)


    if 'County' in filename:
        df = pd.read_csv(path + '/' + filename)

        print('County has {}'.format(len(df)))

        latest_date = df.columns[-1:][0]
        df = df[['RegionName','State','Metro','StateCodeFIPS','MunicipalCodeFIPS',latest_date]].rename(columns={latest_date:'MedianHomePrice'})

        df['StateCodeFIPS'] = df['StateCodeFIPS'].astype(str).str.zfill(2)
        df['MunicipalCodeFIPS'] = df['MunicipalCodeFIPS'].astype(str).str.zfill(3)

        df['Geo_ID'] = df['StateCodeFIPS'] + df['MunicipalCodeFIPS']
        df['Geo_Type'] = 'County'

        df = df.drop(columns=['State','Metro','StateCodeFIPS','MunicipalCodeFIPS'])


        if final_df.empty:
            final_df = df
        else:
            final_df = final_df.append(df)


sql = sql_caller.SqlCaller(create_tables=False)
sql.db_dump_Zillow_MedianHomePrice(final_df)

