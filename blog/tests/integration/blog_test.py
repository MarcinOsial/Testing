from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog("Title blog", "Author blog")
        b.create_post("Test post title", "Test post content")

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, "Test post title")

    def test_json_no_post(self):
        b = Blog("Title blog", "Author blog")

        expected = {
            "title" : "Title blog",
            "author" : "Author blog",
            "posts" : []
        }

        self.assertDictEqual(b.json(), expected)

    def test_json_blog(self):
        b = Blog("Title blog", "Author blog")
        b.create_post("Test post title", "Test post content")

        expected = {
            "title" : "Title blog",
            "author" : "Author blog",
            "posts" : [
                {
                "title": 'Test post title',
                "content": "Test post content"
            }
          ],
        }

        self.assertDictEqual(b.json(), expected)