# The Workshop is presented as set of Slides and Hands-on Exercises

1. [Boriss] Slides INTRO until "Lab - Part I", showing the ALTER TABLE

Hands-on:

    * CREATE TABLE

2. [Boriss] "Lab - Part II" until example with `load_embeddings.py`


Hands-on:

    * Edit Python Template

    * Run Load embedding for chihuahuas and muffins

    * example:

    ./load_embeddings.py /home/dataset/chihuahua_muffin/chihuahua \
                         /var/run /postgresql 5432 p2d2db03 user03


3. [Gülçin] "Lab - Part III" querying

Hands-on:

    * Pick three images: 2 similar and one different, by picking up info from
      the path to the file:

```sql
select id, filename from p2d2.pictures where filename ~ '/chihuahua/' limit 10;

select id, filename from p2d2.pictures where filename ~ '/muffin/' limit 10;
```

    * Test different operators: <-> <+> <=> <#> With SELECT queries

```sql
select embedding <-> (select embedding from p2d2.pictures where id=1)
from p2d2.pictures where id =2;
```

4. [Gülçin] "Lab - Part IV" indexing

Hands-on:

    * Create indexes as in the slides


5. [Boriss] "Lab - Part V" The Challenge

Hands-on:

    * Edit template the_challenge/challenge.py

    * display files with `python3 -m http.server 8042`

    * Use a different vector operator


6. [Boriss-Gülçin] Closing Slides
