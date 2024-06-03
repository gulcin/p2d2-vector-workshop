
Slides INTRO Boriss

    CREATE TABLE

Slides Python load code Boriss

    TODO: Create template and upload it

    Edit Python Template

    Run Load embedding for chihuahuas

    TODO: write command
    ./load_embeddings.py /home/dataset/chihuahua_muffin/chihuahua /var/run /postgresql 5432 p2d2db03 user03


    Run Load embedding for muffins


Slides operators Gülçin

    Pick three images: 2 similar

    Test different operators: <-> <+> <=> <#>
    With SELECT queries

select id, filename from p2d2.pictures where filename ~ '/chihuahua/' limit 10;

select id, filename from p2d2.pictures where filename ~ '/muffin/' limit 10;

select embedding <-> (select embedding from p2d2.pictures where id=1) from p2d2.pictures where id =2;



Slides indexes and search Gülçin

    TODO: Create indexes


Slides Challenge + Python code Boriss

    TODO: Python code to find similar values
    input: challenge image
    output: 10 closest images

    display files with http.server

    Play with operator

Closing Slides
