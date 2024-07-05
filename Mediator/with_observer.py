from abc import ABC, abstractmethod

class UIControl(ABC):

    def __init__(self,):
        self.event_handlers = []
    def add_event_handler(self, observer):
        self.event_handlers.append(observer)
    
    def notify_event_handlers(self):
        for observer in self.event_handlers:
            observer.handle()

class EventHandler(ABC):

    @abstractmethod
    def handle(self):
        pass

class ListBox(UIControl):

    def __init__(self) -> None:
        super().__init__()
        self._selection = None

    @property
    def selection(self):
        return self._selection
    
    @selection.setter
    def selection(self, picked):
        self._selection = picked
        self.notify_event_handlers()
    
class TextBox(UIControl):

    def __init__(self) -> None:
        super().__init__()
        self._content = ""

    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, title):
        self._content = title
        self.notify_event_handlers()

class Button(UIControl):

    def __init__(self) -> None:
        super().__init__()
        self._is_enabled = False

    @property
    def is_enabled(self):
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self, mode):
        self._is_enabled = mode
        self.notify_event_handlers()


class ArticlesDialogBox:

    def __init__(self) -> None:
        self.articles_list_box = ListBox()
        self.title_text_box = TextBox()
        self.save_button = Button()
        self.articles_list_box.add_event_handler(self.create_observer(
            self.article_selected))
        self.title_text_box.add_event_handler(self.create_observer(
            self.title_changed))

    def create_observer(self, handle_method):
        class InlineObserver(EventHandler):
            def handle(self):
                handle_method()
        
        return InlineObserver()
            
    def article_selected(self):  
        self.title_text_box.content = self.articles_list_box.selection
        self.save_button.is_enabled = True
    
    def title_changed(self):
            self.save_button.is_enabled = bool(
                self.title_text_box.content
            )
        
    def simulate_user_interaction(self):
        self.articles_list_box.selection = "article1"
        self.title_text_box.content = ""
        self.articles_list_box.selection = "article2"
        print(f"textbox: {self.title_text_box.content}")
        print(f"button: {self.save_button.is_enabled}")

dialog = ArticlesDialogBox()
dialog.simulate_user_interaction()