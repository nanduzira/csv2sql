# import pandas as pd
import csv
import json
# import numpy as np
import sqlalchemy as sa
import time
import click
import re

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

@click.command(context_settings=CONTEXT_SETTINGS, options_metavar='[options]')
@click.argument('filename', metavar='<FILENAME>', type=click.Path(exists=True))
@click.argument('uri', metavar='<URI>')

def csv_2_sql(filename, uri):
    """
    A BASIC CLI TOOL TO IMPORT STRUCTURED CSV DATA TO A DATABASE.\n
    Arguments :-\n
        <FILENAME> : CSV or Plain-Text File Name with the Data.\n
        <URI> : Database Engine URL.\n
                The url format should be maintained in the format.\n
                e.g : "dialect+driver://username:password@host:port/database"\n
    """

    start_time = time.clock()

    FILENAME=click.format_filename(filename)
    if not FILENAME:
        click.echo(FILENAME)
        click.echo("Command executed in {0:.6f} seconds.".format(time.clock() - start_time))
        exit(0)
    else:
        click.echo("FILENAME : {0}.".format(FILENAME))

    uri_match = re.match(r'^.*://.*:.*@.*:.*/.*$', uri)
    if not uri_match:
        click.echo("{0} doesn't match the URI format of the database.".format(uri))
        click.echo("Command executed in {0:.6f} seconds.".format(time.clock() - start_time))
        exit(0)
    else:
        click.echo("DATABASE URI : {0}.".format(uri))

    engine = sa.create_engine(uri, encoding="utf-8", echo=True)
    con = engine.connect()
    if con:
        click.echo("ENGINE CONNECTED : {0}.".format(con))
    else:
        click.echo("{0} engine can't be connected.".format(con))
        exit(0)

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

    click.echo("Command executed in {0:.6f} seconds.".format(time.clock() - start_time))