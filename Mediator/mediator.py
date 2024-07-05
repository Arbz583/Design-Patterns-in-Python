from abc import ABC, abstractmethod

class UIControl(ABC):

    def __init__(self, owner: "DialogBox") -> None:
        self.owner = owner

class ListBox(UIControl):

    def __init__(self, owner:"DialogBox") -> None:
        super().__init__(owner)
        self._selection = None

    @property
    def selection(self):
        return self._selection
    
    @selection.setter
    def selection(self, picked):
        self._selection = picked
        self.owner.changed(self)
    
class TextBox(UIControl):

    def __init__(self, owner:"DialogBox") -> None:
        super().__init__(owner)
        self._content = ""

    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, title):
        self._content = title
        self.owner.changed(self)

class Button(UIControl):

    def __init__(self, owner:"DialogBox") -> None:
        super().__init__(owner)
        self._is_enabled = False

    @property
    def is_enabled(self):
        return self._is_enabled
    
    @is_enabled.setter
    def is_enabled(self, mode):
        self._is_enabled = mode
        self.owner.changed(self)

class DialogBox(ABC):

    @abstractmethod
    def changed(self, control:UIControl):
        pass

class ArticlesDialogBox(DialogBox):

    def __init__(self) -> None:
        self.articles_list_box = ListBox(self)
        self.title_text_box = TextBox(self)
        self.save_button = Button(self)

    def changed(self, control: UIControl):
        if control == self.articles_list_box:
            self.article_selected()
        elif control == self.title_text_box:
            self.title_changed()
            
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