import unittest
from queryset_gallery.paginator import Paginator


def get_pagination_data(objects_count, page_number, page_count, per_page, errors=False):
    p = {
        'objects_count': objects_count,
        'page_number': page_number,
        'page_count': page_count,
        'per_page': per_page
    }
    not errors or p.update({'errors': 'Page data is invalid'})
    return p


class TestPaginator(unittest.TestCase):

    def test_is_page_valid(self):
        params = ((1, 1, 8, 8, True),  (4, 2, 4, 8, True),  (5, 2, 5, 9, True), (0, 5, 2, 8, False),
                  (1, 1, 0, 0, True),  (2, 1, 0, 0, True),  (1, 2, 0, 0, True), (0, 1, 0, 0, False),
                  (0, 0, 0, 0, False), (1, 0, 0, 0, False), (0, 3, 3, 8, False))
        for p in params:
            self.assertEqual(
                Paginator._is_page_valid(
                    necessary_page=p[0], per_page=p[1], page_count=p[2], objects_count=p[3]
                ), p[4],
                msg=p
            )

    def test_calculate_index(self):
        params = ((1, 1, 1, (0, 1)), (1, 2, 2, (0, 2)), (4, 2, 8, (6, 8)),
                  (8, 1, 8, (7, 8)), (1, 1, 0, (0, 0)))
        for p in params:
            self.assertEqual(
                Paginator._calculate_index(
                    necessary_page=p[0], per_page=p[1], objects_count=p[2]
                ), p[3],
                msg=p
            )

    def test_get_objects_for_page(self):
        objects = [i for i in range(1, 11)]
        params = ((1, 1, [1]), (10, 1, [10]), (5, 2, [9, 10]), (4, 3, [10]), (1, 10, objects))
        for p in params:
            paginator = Paginator(objects=objects, per_page=p[1])
            self.assertEqual(
                paginator._get_objects_for_page(page_number=p[0]), p[2],
                msg=p
            )

    def test_get_page(self):
        objects = [i for i in range(1, 11)]
        params = (
            (1, 1, ([1], get_pagination_data(10, 1, 10, 1))),
            (0, 3, ([], get_pagination_data(10, 0, 4, 3, errors=True))),
            (2, 3, ([4, 5, 6], get_pagination_data(10, 2, 4, 3)))
        )
        for p in params:
            paginator = Paginator(objects=objects, per_page=p[1])
            self.assertEqual(
                paginator.get_page(page_number=p[0]), p[2],
                msg=p
            )


if __name__ == '__main__':
    unittest.main()
