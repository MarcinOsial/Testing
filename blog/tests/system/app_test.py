from unittest import TestCase
from unittest.mock import patch
from blog import Blog
from app import MENU_PROMPT, TITLE_BLOG_INPUT, AUTHOR_BLOG_INPUT
import io
import app
from post import Post


class AppTest(TestCase):

    def test_menu_print_prompts(self):
        with patch("builtins.input") as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)


    def test_menu_calls_print_blogs(self):
        with patch("app.print_blogs") as mocked_print_blogs:
            with patch("builtins.input", return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()


    def test_print_blogs_diffrent(self):
        blog = Blog("Test", "Test author")
        app.blogs = {"Test": blog}
        with patch("builtins.print") as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('* Test by Test author (0 post )')


    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_print_blogs(self, mock_stdout):
    #     blog = Blog("Test", "Test author")
    #     app.blogs = {"Test": blog}
    #     app.print_blogs()
    #     assert mock_stdout.getvalue() == '* Test by Test author (0 post )\n'
    #
    #
    # @patch('builtins.input', return_value=TITLE_BLOG_INPUT)
    # def test_ask_create_blog_title(self, mocked_input):
    #     app.ask_create_blog()
    #     calling = mocked_input()
    #     print(calling)
    #     assert calling == TITLE_BLOG_INPUT
    #
    #
    # @patch('builtins.input', return_value=AUTHOR_BLOG_INPUT)
    # def test_ask_create_blog_author(self, mocked_input):
    #     app.ask_create_blog()
    #     calling = mocked_input()
    #     assert calling == AUTHOR_BLOG_INPUT

    # @patch('builtins.input', return_value=("Test", "Test author"))
    # def test_ask_create_blog_author(self, mocked_input):
    #     app.ask_create_blog()
    #     calling = mocked_input()
    #     assert calling.get('Test') == ("Test", "Test author")


    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test author')
            app.ask_create_blog()
            self.assertIsNotNone(app.blogs.get('Test'))


    def test_ask_read_blog(self):
        blog = Blog("Test", "Test author")
        app.blogs = {"Test": blog}
        with patch("builtins.input", return_value = "Test"):
            with patch("app.print_posts") as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog("Test", "Test author")
        blog.create_post("Title_post", "Content")
        app.blogs = {"Test": blog}
        with patch('app.print_post') as mocked_print_post:
            app.print_posts(blog)
            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post("Title_post", "Content_post")
        expected_print = """
    =========== Title_post ===========
    
    Content_post
    
    """
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)

    def test_ask_create_post(self):
        blog = Blog("Test", "Test author")
        app.blogs = {"Test": blog}
        with patch("builtins.input") as mocked_input:
            mocked_input.side_effect = ('Test', 'Title_post', 'Content')
            app.ask_create_post()
            self.assertEqual(blog.posts[0].title,'Title_post')
            self.assertEqual(blog.posts[0].content, 'Content' )
            self.assertEqual(blog.title,'Test')