class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,value):
        if type(value) == str and value != "":
            if not hasattr(self,"title"):
                self._title = value

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,value):
        if type(value) == Author:
            self._author = value

    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self,value):
        if type(value) == Magazine:
            self._magazine = value
        
class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def articles(self):
        return [art for art in Article.all if art.author == self]

    def magazines(self):
        return list({art.magazine for art in Article.all if art.author == self})

    def add_article(self, magazine, title):
        return Article(author=self,magazine=magazine,title=title)

    def topic_areas(self):
        li = list({art.magazine.category for art in Article.all if art.author == self})
        if len(li) > 0:
            return li
        return None

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if type(value) == str and value != "":
            if not hasattr(self,"name"):
                self._name = value

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        return [art for art in Article.all if art.magazine == self]

    def contributors(self):
        return list({art.author for art in Article.all if art.magazine == self})

    def article_titles(self):
        titles = [art.title for art in Article.all if art.magazine == self]
        return titles if len(titles) > 0 else None

    def contributing_authors(self):
        s1 = set()
        s2 = set()
        return_set = set()
        for art in self.articles():
            if art.author in s1:
                if art.author in s2:
                    return_set.add(art.author)
                else:
                    s2.add(art.author)
            else:
                s1.add(art.author)
        return return_set if len(return_set) > 0 else None


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if type(value) == str and len(value) <= 16 and len(value) >= 2:
            self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,value):
        if type(value) == str and value != "":
            self._category = value