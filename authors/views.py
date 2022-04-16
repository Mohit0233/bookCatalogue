from rest_framework import views

from authors import service
from authors.serializers import AddAuthorSerializers
from rest_framework.response import Response as RestResponse


# addAnAuthor(<author>)
# getAllAuthorName()

class AddAnAuthor(views.APIView):
    """
        addAnAuthor(<author>)
    """

    def post(self, request):

        serializer_data = AddAuthorSerializers(data=request.data)
        serializer_data.is_valid(raise_exception=True)

        if service.get_author(serializer_data.validated_data.get('authorId')):
            return RestResponse("Author already exists", 200)

        if service.add_author(**serializer_data.validated_data):
            return RestResponse("Success", 200)
        else:
            return RestResponse("Failed to add author", 200)


class GetAllAuthorName(views.APIView):
    """
        getAllAuthorName()
    """

    def get(self, request):

        author_list = service.get_all_author_name()
        return RestResponse(author_list, 200)
