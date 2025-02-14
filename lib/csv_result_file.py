from lib.result_file import ResultFile

class CsvResultFile(ResultFile):
    def __init__(self, file_name):
        super().__init__(file_name)
        file1 = open(self.file_name, "w")
        header = "Type,Endpoint,Time,Result\n"
        file1.writelines(header)
        file1.close()

    def add_row(self, row_data):
        result_row = "{name},{url},{time},{response_code}\n".format(
            name = row_data['name'],
            url = row_data['url'],
            time = row_data['time'],
            response_code = row_data['responseCode']['code']
        )
        file1 = open(self.file_name, "a")
        file1.write(result_row)
        file1.close()
