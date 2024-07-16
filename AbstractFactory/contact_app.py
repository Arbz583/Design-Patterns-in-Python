from abstract_factory import WidgetFactory, MaterialWidgetFactory, AntWidgetFactory

class ContactForm:

    def render(self, factory: WidgetFactory):

        button = factory.create_button()
        button.render()

        text_box = factory.create_text()
        text_box.render()

form = ContactForm()
form.render(MaterialWidgetFactory())
form.render(AntWidgetFactory())