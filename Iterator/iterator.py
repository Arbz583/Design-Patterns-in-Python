class BrowseHistory:
    
    def __init__(self) -> None:
        self.urls = []

    def push(self, url):
        self.urls.append(url)

    def pop(self):
        return self.urls.pop()

    def create_iterable(self):
        return self.ListIterator(self)
    
    class ListIterator:

        def __init__(self, browsehistory) -> None:
            self.browsehistory = browsehistory
            self.index = 0
            
        def has_next(self):
            return self.index < len(self.browsehistory.urls)

        def current(self):
            return self.browsehistory.urls[self.index]
             
        def next(self):
            self.index+=1

browsehistory_1 = BrowseHistory()
browsehistory_1.push("a")
browsehistory_1.push("b")
browsehistory_1.push("c")
iterable = browsehistory_1.create_iterable()

while iterable.has_next():
    print(iterable.current())
    iterable.next()