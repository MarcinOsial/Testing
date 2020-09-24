from unittest import TestCase
from post import Post


class PostTest(TestCase):
    def test_create_post(self):
        p = Post("tittle post", "content post")

        self.assertEqual("tittle post", p.title)
        self.assertEqual("content post", p.content)

    def test_json(self):
        p2 = Post("tittle post", "content post")
        expected = {
            "title": 'tittle post',
            "content": "content post"
        }
        self.assertDictEqual(p2.json(), expected)
