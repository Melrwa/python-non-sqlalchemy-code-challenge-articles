class Article:
    all = []  # Store all the articles by authors

    def __init__(self, author: str, magazine: str, title: str):
        # Checking if the article to be added meets the required conditions
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)  # Append the article to the all list


class Author:
    def __init__(self, name):
        # Ensures the name of the author is a string
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        self._name = name

    @property
    def name(self):
        # Returns the name of the author
        return self._name

    @name.setter
    def name(self, value):
        # Prevents modification of the author's name
        raise AttributeError("Name is immutable and cannot be changed.")

    def articles(self):
        # Returns all articles written by the author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Returns a unique list of magazines this author has contributed to
        return list(set(article.magazine for article in self.articles()))  

    def add_article(self, magazine, title):
        # Creates and associates a new article to the author
        return Article(self, magazine, title)

    def topic_areas(self):
        # Return unique categories of magazines this author has written about
        magazines = self.magazines()
        if not magazines:
            return None  # Return None if the author has no articles
        return list(set(magazine.category for magazine in magazines))


class Magazine:
    all_magazines = []  # Store all magazine instances

    def __init__(self, name, category):
        # Ensures the magazine name and category are valid strings
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        if not isinstance(category, str):
            raise ValueError("Category must be a string.")
        
        self._name = name
        self._category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        # Returns the name of the magazine
        return self._name

    @name.setter
    def name(self, value):
        # Ensures the magazine name is between 2 and 16 characters
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        # Returns the category of the magazine
        return self._category

    @category.setter
    def category(self, value):
        # Ensures the category is a non-empty string
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        # Returns all articles published in this magazine
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Returns a list of unique authors who have written for the magazine
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        # Returns the titles of all articles in the magazine
        titles = [article.title for article in self.articles()]
        return None if not titles else titles

    def contributing_authors(self):
        # Returns authors who have contributed more than twice to the magazine
        author_counts = {author: 0 for author in self.contributors()}
        for article in self.articles():
            author_counts[article.author] += 1
        result = [author for author, count in author_counts.items() if count > 2]
        return None if not result else result
