from rest_framework import views

# addBookToCatalog(<book>)
# addCategory(<category ID>,<category name>)
# getListOfCategories()
# getMostBooksSoldByAuthor(<author ID>)
# getMostBooksSoldByCategory(<category ID>)
# searchBook(<by_partial_title/by_partial_author_name> or both)
# getBooksByAuthor(<author ID>)


class AddBookToCatalog(views.APIView):
    """
        addBookToCatalog(<book>)
    """

    def post(self):
        pass


class AddCategory(views.APIView):
    """
        addCategory(<category ID>,<category name>)    
    """

    def post(self):
        pass


class GetListOfCategories(views.APIView):
    """
        getListOfCategories()    
    """

    def get(self):
        pass


class GetMostBooksSoldByAuthor(views.APIView):
    """
        getMostBooksSoldByAuthor(<author ID>)    
    """

    def get(self):
        pass


class GetMostBooksSoldByCategory(views.APIView):
    """
        getMostBooksSoldByCategory(<category ID>)    
    """

    def get(self):
        pass


class SearchBook(views.APIView):
    """
        searchBook(<by_partial_title/by_partial_author_name> or both)    
    """

    def get(self):
        pass


class GetBooksByAuthor(views.APIView):
    """
        getBooksByAuthor(<author ID>)    
    """

    def get(self):
        pass
