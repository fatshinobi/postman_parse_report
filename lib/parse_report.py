import ijson

class ParseReport:
    def __init__(self, json_file):
        self.file_name = json_file

    def read_file(self, result_file):
        with open(self.file_name, 'r') as file:
            objects = ijson.items(file, 'results.item')
            for item in objects:
                result_file.add_row(item)
