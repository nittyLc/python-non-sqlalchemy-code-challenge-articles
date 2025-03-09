import unittest
from lib.debug import Author, Article, Magazine

class TestArticle(unittest.TestCase):
    def setUp(self):
        self.author = Author("John Doe")
        self.magazine = Magazine("Tech Monthly", "Technology")
        self.article = Article(self.author, self.magazine, "The Future of AI")

    def test_article_creation(self):
        self.assertEqual(self.article.title, "The Future of AI")
        self.assertEqual(self.article.author, self.author)
        self.assertEqual(self.article.magazine, self.magazine)

    def test_article_title_immutable(self):
        with self.assertRaises(AttributeError):
            self.article.title = "New Title"

class TestAuthor(unittest.TestCase):
    def setUp(self):
        self.author = Author("John Doe")
        self.magazine = Magazine("Tech Monthly", "Technology")

    def test_author_creation(self):
        self.assertEqual(self.author.name, "John Doe")

    def test_add_article(self):
        article = self.author.add_article(self.magazine, "The Future of AI")
        self.assertIn(article, self.author.articles())
        self.assertIn(article, self.magazine.articles())

    def test_magazines(self):
        self.author.add_article(self.magazine, "The Future of AI")
        self.assertIn(self.magazine, self.author.magazines())

    def test_topic_areas(self):
        self.author.add_article(self.magazine, "The Future of AI")
        self.assertIn("Technology", self.author.topic_areas())

class TestMagazine(unittest.TestCase):
    def setUp(self):
        self.author = Author("John Doe")
        self.magazine = Magazine("Tech Monthly", "Technology")
        self.article = Article(self.author, self.magazine, "The Future of AI")
        self.magazine._articles.append(self.article)

    def test_magazine_creation(self):
        self.assertEqual(self.magazine.name, "Tech Monthly")
        self.assertEqual(self.magazine.category, "Technology")

    def test_articles(self):
        self.assertIn(self.article, self.magazine.articles())

    def test_contributors(self):
        self.assertIn(self.author, self.magazine.contributors())

    def test_article_titles(self):
        self.assertIn("The Future of AI", self.magazine.article_titles())

    def test_contributing_authors(self):
        self.magazine._articles.append(Article(self.author, self.magazine, "AI in 2025"))
        self.assertIn(self.author, self.magazine.contributing_authors())

if __name__ == '__main__':
    unittest.main()