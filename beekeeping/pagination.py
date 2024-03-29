from rest_framework import pagination


class DjangoLessonPaginationClass(pagination.PageNumberPagination):
    page_size = 10
    max_page_size = 100
    page_size_query_param = "size"
