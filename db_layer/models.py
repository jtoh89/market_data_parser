from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, MetaData, create_engine, Column, Integer, String, Float, BigInteger, Date
import datetime

Base = declarative_base()


class Zillow_MedianHomePrice(Base):
    __tablename__ = "Zillow_MedianHomePrice"
    Geo_ID = Column(String(10), unique=False, primary_key=True)
    Geo_Type = Column(String(50), unique=False)
    RegionName = Column(String(50), unique=False)
    MedianHomePrice = Column(Integer, unique=False)

# class Zillow_County_MedianHomePrice(Base):
#     __tablename__ = "Zillow_County_MedianHomePrice"
#     Geo_ID = Column(String(10), unique=False, primary_key=True)
#     Geo_Type = Column(String(50), unique=False)
#     RegionName = Column(String(50), unique=False)
#     MedianHomePrice = Column(Integer, unique=False)
#
#
#
# class Zillow_Zipcode_MedianHomePrice(Base):
#     __tablename__ = "Zillow_Zipcode_MedianHomePrice"
#     Geo_ID = Column(String(10), unique=False, primary_key=True)
#     Geo_Type = Column(String(50), unique=False)
#     RegionName = Column(String(50), unique=False)
#     MedianHomePrice = Column(Integer, unique=False)


class Zillow_MSAID_Lookup(Base):
    __tablename__ = "Zillow_MSAID_Lookup"
    Zillow_Id = Column(String(10), unique=False, primary_key=True)
    Zillow_MSA_Name = Column(String(50), unique=False)
    Geo_ID = Column(String(10), unique=False)
    MSA_Name = Column(String(50), unique=False)

class InitiateDeclaratives():
    @staticmethod
    def create_tables(engine_string):
        engine = create_engine(engine_string)
        Base.metadata.create_all(engine)


