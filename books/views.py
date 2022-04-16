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
    """

    def post(self, request):
        serializer_object = serializers.BookSerializer(data=request.data)
        serializer_object.is_valid(raise_exception=True)

        return service.get_or_add_book(**serializer_object.validated_data)


class AddCategory(views.APIView):
    """
        addCategory(<category ID>,<category name>)    
    """

    def post(self, request):
        serializer_object = serializers.CategorySerializer(data=request.data)
        serializer_object.is_valid(raise_exception=True)

        if service.add_category(**serializer_object.validated_data):
            return RestResponse("Success", 200)
        else:
            return RestResponse('Failed to add category', 400)


class GetListOfCategories(views.APIView):
    """
        getListOfCategories()    
    """

    def get(self, request):
        categories_list = service.get_list_of_categories()
        return RestResponse(categories_list, 200)


class GetMostBooksSoldByAuthor(views.APIView):
    """
        getMostBooksSoldByAuthor(<author ID>)    
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
    """

    def get(self, request):
        serializer_object = serializers.AuthorIdSerializer(data=request.query_params)
        serializer_object.is_valid(raise_exception=True)

        book_id_list = service.get_books_by_author(author_id=serializer_object.validated_data.get('authorId'))

        return RestResponse(book_id_list, 200)
