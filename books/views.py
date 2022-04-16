from rest_framework import views
from books import service, serializers
from rest_framework.response import Response as RestResponse

# addBookToCatalog(<book>)
# addCategory(<category ID>,<category name>)
# getListOfCategories()
# getMostBooksSoldByAuthor(<author ID>)
# getMostBooksSoldByCategory(<category ID>)
# searchBook(<by_partial_title/by_partial_author_name> or both)
# getBooksByAuthor(<author ID>)
from books.serializers import serialize_python_object_to_json


class AddBookToCatalog(views.APIView):
    """
        addBookToCatalog(<book>)

        get or add book to catalog

        Example Api Call

        POST /book/addBookToCatalog HTTP/1.1
        Host: 127.0.0.1:8000
        Content-Type: application/json
        Content-Length: 233

        {
            "bookId": "Book6",
            "title": "Red Blue Gree",
            "authorId": "Author1",
            "publisher": "Gutenberg",
            "publishDate": "1-Jan-2000",
            "categoryId": "Category1",
            "price": "200",
            "soldCount": "9999990"
        }

    """

    def post(self, request):
        serializer_object = serializers.BookSerializer(data=request.data)
        serializer_object.is_valid(raise_exception=True)

        message, status_code = service.get_or_add_book(**serializer_object.validated_data)
        return RestResponse(data=message, status=status_code)


class AddCategory(views.APIView):
    """
        addCategory(<category ID>,<category name>)

        get or add category

        Example Api Call

        POST /book/addCategory HTTP/1.1
        Host: 127.0.0.1:8000
        Content-Type: application/json
        Content-Length: 65

        {
            "categoryId": "Category3",
            "categoryName": "drama"
        }

    """

    def post(self, request):
        serializer_object = serializers.CategorySerializer(data=request.data)
        serializer_object.is_valid(raise_exception=True)

        category_object, is_created = service.get_or_add_category(**serializer_object.validated_data)

        if category_object:
            if is_created:
                return RestResponse("Success", 200)
            else:
                return RestResponse("Already Created", 200)
        else:
            return RestResponse('Failed to add category', 400)


class GetListOfCategories(views.APIView):
    """
        getListOfCategories()

        get list of all categories

        Example Api Call

        GET /book/getListOfCategories HTTP/1.1
        Host: 127.0.0.1:8000

    """

    def get(self, request):
        categories_list = service.get_list_of_categories()
        return RestResponse(categories_list, 200)


class GetMostBooksSoldByAuthor(views.APIView):
    """
        getMostBooksSoldByAuthor(<author ID>)

        get most books sold by author by soldCount

        Example Api Call

        GET /book/getMostBooksSoldByAuthor?authorId=Author1 HTTP/1.1
        Host: 127.0.0.1:8000

    """

    def get(self, request):
        serializer_object = serializers.AuthorIdSerializer(data=request.query_params)
        serializer_object.is_valid(raise_exception=True)

        book_object = service.get_most_books_sold_by_author(author_id=serializer_object.validated_data.get('authorId'))

        if book_object:
            return RestResponse(serialize_python_object_to_json(book_object), 200)
        else:
            return RestResponse("Unable to find the book", 400)


class GetMostBooksSoldByCategory(views.APIView):
    """
        getMostBooksSoldByCategory(<category ID>)

        gets the Most Sold book by search for category_id

        Example Api Call

        GET /book/getMostBooksSoldByCategory?categoryId=Category1 HTTP/1.1
        Host: 127.0.0.1:8000

    """

    def get(self, request):
        serializer_object = serializers.CategoryIdSerializer(data=request.query_params)
        serializer_object.is_valid(raise_exception=True)

        book_object = service.get_most_books_sold_by_category(
            category_id=serializer_object.validated_data.get('categoryId'))

        if book_object:
            return RestResponse(serialize_python_object_to_json(book_object), 200)
        else:
            return RestResponse("Unable to find the book", 400)


class SearchBook(views.APIView):
    """
        searchBook(<by_partial_title/by_partial_author_name> or both)

        checks if title contains partial title or author contains author name

        Example Api Call

        GET /book/searchBook?partialTitle=Green&partialAuthorName=Author2 HTTP/1.1
        Host: 127.0.0.1:8000


    """

    def get(self, request):
        serializer_object = serializers.PartialTitlePartialAuthorNameSerializer(data=request.query_params)
        serializer_object.is_valid(raise_exception=True)

        book_object_list = service.search_book(partial_title=serializer_object.validated_data.get('partialTitle'),
                                               partial_author_name=serializer_object.validated_data.get(
                                                   'partialAuthorName'))
        return RestResponse(serialize_python_object_to_json(book_object_list), 200)


class GetBooksByAuthor(views.APIView):
    """
        getBooksByAuthor(<author ID>)

        gets the books_id by author name

        Example Api Call

        GET /book/getBooksByAuthor?authorId=Author1 HTTP/1.1
        Host: 127.0.0.1:8000


    """

    def get(self, request):
        serializer_object = serializers.AuthorIdSerializer(data=request.query_params)
        serializer_object.is_valid(raise_exception=True)

        book_id_list = service.get_books_by_author(author_id=serializer_object.validated_data.get('authorId'))

        return RestResponse(book_id_list, 200)
