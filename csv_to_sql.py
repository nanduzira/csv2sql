# import pandas as pd
import csv
import json
# import numpy as np
# import sqlalchemy as sa
import time
import click
import os

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS, options_metavar='<options>')
@click.argument('filename', metavar='<FILENAME>')

def csv_2_sql(filename):
    """ A BASIC CLI TOOL TO IMPORT STRUCTURED CSV DATA TO A DATABASE """
    start_time = time.clock()
    FILEPATH = os.path.join(os.getcwd(), filename)
    print(FILEPATH)
    # MODIFY_CSV = "./datasets/title.principals.0.csv"

    # CONFIG_JSON = "./conf/db_info.json"
    # with open(CONFIG_JSON,'r') as fp:
    #     db_info = json.load(fp)
    # ENGINE_URL = db_info['type']+"://"+db_info['user']+":"+db_info['pass']+"@"+db_info['host']+":"+db_info['port']+"/"+db_info['name']+"?charset=utf8"
    # print ENGINE_URL

    # engine = sa.create_engine(ENGINE_URL, encoding="utf-8", echo=True)
    # con = engine.connect()

    # with open(FILENAME, 'rb') as csvfile:
    #     spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    #     temp_csv_list = list(spamreader)
    #     del(spamreader)
        
    #     data = pd.DataFrame(temp_csv_list[1:], columns=temp_csv_list[0])
    #     del(temp_csv_list)
    #     print data.info()
    #     print np.where(pd.isnull(data))

    #     data = data.replace('\N', np.NaN)

    #     print data.isnull().sum()

    #     data.to_csv(MODIFY_CSV, index=False)

    # chunks = pd.read_csv(MODIFY_CSV, chunksize=100000, index_col=0)

    # TABLE_NAME = "TITLE_PRINCIPALS"
    # try:
    #     for chunk in chunks:
    #         print chunk
    #         chunk.to_sql(name=TABLE_NAME, con=con, if_exists="append")
    #     con.close()
    # except Exception, e:
    #     print "EXCEPTION", e

    print("Transfer completed in {0:.6f} seconds>".format(time.clock() - start_time))