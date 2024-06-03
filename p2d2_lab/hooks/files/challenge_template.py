#! /usr/bin/env python3

import sys
from PIL import Image
from imgbeddings import imgbeddings
import psycopg2

def main():
    search_img = sys.argv[1]
    the_host = sys.argv[2] if len(sys.argv) > 2  else "localhost"
    the_port = sys.argv[3] if len(sys.argv) > 3  else "5432"
    the_dbname = sys.argv[4] if len(sys.argv) > 4  else "hackathon"
    the_user = sys.argv[5] if len(sys.argv) > 5  else "postgres"

    # open the challenge image
    img = Image.open(search_img)
    # load the `imgbeddings`
    ibed = imgbeddings()
    # calculating the embeddings
    embedding = ibed.to_embeddings(img)

    conn = psycopg2.i#TODO(host=the_host,
                            port=the_port,
                            dbname=the_dbname,
                            user=the_user)

    cur = conn.#TODO()
    string_representation = "["+ ",".join(str(x) for x in embedding[0].tolist()) +"]"
    cur.execute("""
                SELECT filename AS image, embedding #TODO %s AS proximity
                FROM p2d2.pictures
                ORDER BY proximity LIMIT 10
                """
                , (string_representation,))
    rows = cur.#TODO()

    with open('index.html', 'w') as result:
        result.write('<html>\n<body>\n')
        result.write('<h2>Challenge</h2>\n')
        result.write('<img src="%s" />\n' % search_img)
        result.write('<h2>Found</h2>\n')
        for row in rows:
            result.write('<img src="%s" width="150" />' % row[0])
        result.write('\n</body>\n</html>\n')

    cur.#TODO()

    print(sys.argv[0])


if __name__ == '__main__':
    main()
