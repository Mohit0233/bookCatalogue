# bookCatalogue



## Setup

The first thing to do is to **clone the repository**:

```shell
git clone https://github.com/Mohit0233/bookCatalogue.git
cd bookCatalogue
```


Create a **virtual environment** to install dependencies in and activate it:

```shell
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

or using venv https://docs.python.org/3/library/venv.html#creating-virtual-environments

Then install the dependencies:

```shell
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```

Django version 4.0.4, using settings 'bookCatalogue.settings'

Starting development server at http://127.0.0.1:8000/


## Postman Collection
[PostmanCollection: bookCatalogue.postman_collection.json](bookCatalogue.postman_collection.json)


[How to impot Postman Collection?](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-data-into-postman)


## Api Call Mapping

```http request
http://127.0.0.1:8000/book/addBookToCatalog
http://127.0.0.1:8000/book/addCategory
http://127.0.0.1:8000/book/getListOfCategories
http://127.0.0.1:8000/book/getMostBooksSoldByAuthor?authorId=Author1
http://127.0.0.1:8000/book/getMostBooksSoldByCategory?categoryId=Category1
http://127.0.0.1:8000/book/searchBook?partialTitle=Green&partialAuthorName=Author2
http://127.0.0.1:8000/book/getBooksByAuthor?authorId=Author1
http://127.0.0.1:8000/author/addAnAuthor
http://127.0.0.1:8000/author/getAllAuthorName
```
