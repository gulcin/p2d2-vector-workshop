#! /usr/bin/env python3

import sys
import numpy as np
from imgbeddings import imgbeddings
from PIL import Image
import psycopg2
import os


def main():
    # arguments
    # 1 - directory where images are stored
    # 2 - hostname of the database
    # 3 - port number
    # 4 - database name
    # 5 - username
    source_dir = sys.argv[1]
    the_host = sys.argv[2] if len(sys.argv) > 2  else "localhost"
    the_port = sys.argv[3] if len(sys.argv) > 3  else "5432"
    the_dbname = sys.argv[4] if len(sys.argv) > 4  else "postgres"
    the_user = sys.argv[5] if len(sys.argv) > 5  else "postgres"

    conn = psycopg2.connect(host=the_host,
                            port=the_port,
                            dbname=the_dbname,
                            user=the_user)

    # load the imgbeddings
    ibed = imgbeddings()
    for filename in os.listdir(source_dir):
        image_path = source_dir + "/" + filename
        # open the image
        img = Image.open(image_path)
        # calculate the embeddings
        embedding = ibed.to_embeddings(img)
        cur = conn.cursor()
        cur.execute("INSERT INTO p2d2.pictures (filename, embedding) values (%s, %s)",
                    (image_path, embedding[0].tolist()))
        print(image_path)
        conn.commit()

    print("Done!")


if __name__ == '__main__':
    main()
