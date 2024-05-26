class Article:
    #class attribute to store all the instances
    my_list = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
        #appends the current instance (self) to the list my_list belonging to the class.
        self.__class__.my_list.append(self)
      
      
class Author:
    my_list = []
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        self.__class__.my_list.append(self)

    @property
    def name(self):
        """The name property"""
        return self._name

    def articles(self):
        return [article for article in Article.my_list if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = {article.magazine.category for article in Article.my_list if article.author == self}
        return list(categories) if categories else None


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Names must be between 2 and 16 characters")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Categories must be of type str and must be longer than 0 characters")
        self._name = name
        self._category = category

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, name):
        """Name must be a string between 2 and 16 characters in length"""
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise ValueError("Names must be between 2 and 16 characters")
        self._name = name

    @property
    def category(self):
        """The category property"""
        return self._category

    @category.setter
    def category(self, category):
        """Categories must be of type str"""
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Magazine category must be a non-empty string.")
        self._category = category
        
    def articles(self):
        return [article for article in Article.my_list if article.magazine == self]

    def contributors(self):
         return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [article.author for article in self.articles]
        return [author for author in set(authors) if authors.count(author) > 2] or None