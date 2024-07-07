from abc import ABC, abstractmethod

class Operation(ABC):

    @abstractmethod
    def apply(self, document:"HtmlDocument"):
        pass


class HighLoghtOperation(Operation):

    def apply(self, document:"HtmlDocument"):
        if isinstance(document, HeadingNode):
            print("heading be highlighted")
        elif isinstance(document, AnchorNode):
            print("anchor be highlited")

class PlainTextOperation(Operation):

    def apply(self, document:"HtmlDocument"):
        if isinstance(document, HeadingNode):
            print("be extracted text from heading")
        elif isinstance(document, AnchorNode):
            print("be extracted text from highlited")

class HtmlNode(ABC):

    @abstractmethod
    def execute(self, operation:Operation):
        pass


class HeadingNode(HtmlNode):

    def execute(self, operation: Operation):
        operation.apply(self)

class AnchorNode(HtmlNode):
    def execute(self, operation: Operation):
        operation.apply(self)

class HtmlDocument:

    def __init__(self) -> None:
        self.nodes = []
    
    def add(self, node:HtmlNode):
        self.nodes.append(node)
    
    def execute(self, operation:Operation):
        for node in self.nodes:
            node.execute(operation)

document = HtmlDocument()
document.add(HeadingNode())
document.add(AnchorNode())
document.execute(HighLoghtOperation())
document.execute(PlainTextOperation())