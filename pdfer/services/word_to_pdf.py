from docx2pdf import convert
from .. import utils
from .base_service import Action


class WordToPdf(Action):
    command = "word2pdf"
    doc = "Перевожу doc(x) в PDF, аргументы - файлы"

    def run_action(self):
        for file in self.params:
            output = utils.OUTPUT_PATH / f"{utils.get_random_name()}.pdf"
            convert(file, output_path=str(output))
