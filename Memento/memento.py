class EditorState:
    def __init__(self, title) -> None:
        self._content = title
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, title):
        self._content = title

class Editor:
    def __init__(self) -> None:
        self._content = None
    
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, title):
        self._content = title

    def create_state(self):
        return EditorState(self.content)

    def restore_state(self, state):
        self._content = state.content

class History:
    def __init__(self) -> None:
        self.states = []

    def push(self, state):
        self.states.append(state)
    
    def pop(self):
        return self.states.pop()
    
editor = Editor()
history = History()

editor.content = "a"
history.push(editor.create_state())
editor.content = "b"
history.push(editor.create_state())
editor.content = "c"
editor.restore_state(history.pop())
editor.restore_state(history.pop())

print(editor.content)