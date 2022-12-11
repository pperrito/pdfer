import pdf2docx
from .. import utils
from .base_service import Action


class PdfToWord(Action):
    command = "pdf2word"
    doc = "Перевожу (пытаюсь) pdf в doc(x), аргументы - файлы"

    def run_action(self):
        for file in self.params:
            output = utils.OUTPUT_PATH / f"{utils.get_random_name()}.docx"
            conv = pdf2docx.Converter(file)
            conv.convert(str(output))
