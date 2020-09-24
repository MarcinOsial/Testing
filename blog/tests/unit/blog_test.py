from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Title blog", "Author blog")
        self.assertEqual("Title blog", b.title)
        self.assertEqual("Author blog", b.author)
        self.assertListEqual([], b.posts)

    def test_reprr(self):
        b = Blog("Title blog", "Author blog")

        self.assertEqual(b.__repr__(), "Title blog by Author blog (0 post )")

    def test_reprr_multiple_posts(self):
        b = Blog("Title blog", "Author blog")
        b.posts = ['test']
        b2 = Blog("John title", "Oliver author")
        b2.posts = ["test", "another"]

        self.assertEqual(b.__repr__(),"Title blog by Author blog (1 posts)")
        self.assertEqual(b2.__repr__(),"John title by Oliver author (2 posts)")

    def test_create_post_in_blog(self):
        b = Blog("Title blog", "Author blog")
        b.create_post("Test post title", "Test post content")

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, "Test post title")
