from rest_framework import views


# addAnAuthor(<author>)
# getAllAuthorName()

class AddAnAuthor(views.APIView):
    """
        addAnAuthor(<author>)
    """

    def post(self):
        pass


class GetAllAuthorName(views.APIView):
    """
        getAllAuthorName()
    """

    def get(self):
        pass
