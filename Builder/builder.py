from abc import ABC, abstractmethod
from typing import List

class Slide:

    def __init__(self, text:str) -> None:
        self._text = text
    
    @property
    def text(self) -> str:
        return self._text
    
    
class PdfDocument:

    def add_page(self, text:str):
        print(f" Adding a {text} page to PDF")
        # then save this page in a list in current obj

class Movie:

    def add_frame(self, text:str, duration: int):
        print(f"Adding a {text} frame to movie")


class PresentationBuilder(ABC):

    @abstractmethod
    def add_slide(self, slide: Slide) -> None:
        pass

class PdfDocumentBuilder(PresentationBuilder):

    def __init__(self, document:PdfDocument) -> None:
        self.document = document
    
    def add_slide(self, slide: Slide) -> None:
        self.document.add_page(slide.text)
    
    def get_pdf_document(self):
        return self.document
    

class MovieBuilder(PresentationBuilder):

    def __init__(self, movie: Movie) -> None:
        self.movie = movie
    
    def add_slide(self, slide: Slide) -> None:
        self.movie.add_frame(slide.text, 3)
    
    def get_movie(self):
        return self.movie

class Presentation:

    def __init__(self) -> None:
        self.slides : List[Slide] = []
    
    def add_slide(self, slide: Slide) -> None:
        self.slides.append(slide)
    
    def export(self, builder: PresentationBuilder) -> None:
        builder.add_slide(Slide("Copyright Notice"))
        for slide in self.slides:
            builder.add_slide(slide)

presntation = Presentation()
presntation.add_slide(Slide("Slide 1"))
presntation.add_slide(Slide("Slide 2"))

builder = PdfDocumentBuilder(PdfDocument())
presntation.export(builder)
pdf = builder.get_pdf_document()

builder = MovieBuilder(Movie())
presntation.export(builder)
movie = builder.get_movie()