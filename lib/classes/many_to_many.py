class Article:
    """
    Represents an Article with an associated Author, Magazine, and Title.
    Tracks all articles created in the application.
    """
    all = []  # Store all articles globally

    def __init__(self, author, magazine, title):
        """
        Initialize an Article instance.
        :param author: Author instance
        :param magazine: Magazine instance
        :param title: str, must be 5-50 characters long
        """
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")
        
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)  # Register the article globally


class Author:
    """
    Represents an Author who writes articles for magazines.
    Tracks the relationship between the Author and their articles or magazines.
    """
    def __init__(self, name):
        """
        Initialize an Author instance.
        :param name: str, name of the author
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        self._name = name

    @property
    def name(self):
        """Return the name of the author."""
        return self._name

    @name.setter
    def name(self, value):
        """Prevent modification of the author's name."""
        raise AttributeError("Name is immutable and cannot be changed.")

    def articles(self):
        """Return all articles written by the author."""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Return unique magazines the author has contributed to."""
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        """
        Create a new article associated with the author.
        :param magazine: Magazine instance
        :param title: str
        :return: New Article instance
        """
        return Article(self, magazine, title)

    def topic_areas(self):
        """
        Return unique categories of magazines the author has written for.
        :return: List of unique categories or None if no articles exist.
        """
        magazines = self.magazines()
        return None if not magazines else list(set(magazine.category for magazine in magazines))


class Magazine:
    """
    Represents a Magazine, which contains articles by various authors.
    Tracks all magazine instances and their relationships with articles and authors.
    """
    all_magazines = []  # Store all magazines globally

    def __init__(self, name, category):
        """
        Initialize a Magazine instance.
        :param name: str, name of the magazine
        :param category: str, category of the magazine
        """
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not isinstance(category, str):
            raise ValueError("Category must be a string.")

        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        """Return the name of the magazine."""
        return self._name

    @name.setter
    def name(self, value):
        """Set the name of the magazine with validation."""
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        """Return the category of the magazine."""
        return self._category

    @category.setter
    def category(self, value):
        """Set the category of the magazine with validation."""
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        """Return all articles published in this magazine."""
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Return unique authors who have written for this magazine."""
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        """
        Return the titles of all articles in this magazine.
        :return: List of titles or None if no articles exist.
        """
        titles = [article.title for article in self.articles()]
        return None if not titles else titles

    def contributing_authors(self):
        """
        Return authors who have contributed more than twice to the magazine.
        :return: List of contributing authors or None if no such authors exist.
        """
        author_counts = {author: 0 for author in self.contributors()}
        for article in self.articles():
            author_counts[article.author] += 1
        result = [author for author, count in author_counts.items() if count > 2]
        return None if not result else result

    @classmethod
    def top_publisher(cls):
        """
        Return the magazine with the most articles.
        :return: Magazine instance with the most articles or None if no articles exist.
        """
        if not Article.all:
            return None
        magazine_counts = {magazine: 0 for magazine in cls.all_magazines}
        for article in Article.all:
            magazine_counts[article.magazine] += 1
        return max(magazine_counts, key=magazine_counts.get)


# Example Usage

# Create authors
author1 = Author("Melki")
author2 = Author("Alare")

# Create magazines
magazine1 = Magazine("Tech Today", "Technology")
magazine2 = Magazine("Health & Wellness", "Health")

# Add articles
article1 = author1.add_article(magazine1, "The Future of AI")
article2 = author1.add_article(magazine1, "Exploring Robotics")
article3 = author2.add_article(magazine2, "Healthy Living Tips")

# Author methods
print(author1.articles())  # List of articles by Melki
print(author1.magazines())  # List of magazines Melki has contributed to
print(author1.topic_areas())  # List of unique categories Melki has written about

# Magazine methods
print(magazine1.articles())  # List of articles in Tech Today
print(magazine1.contributors())  # List of contributors to Tech Today
print(magazine1.article_titles())  # Titles of articles in Tech Today
print(magazine1.contributing_authors())  # Authors with more than two contributions

# Class method
print(Magazine.top_publisher())  # Magazine with the most articles
