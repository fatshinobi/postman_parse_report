from lib.result_file import ResultFile
import fpdf

class PdfResultFile(ResultFile):
    def __init__(self, file_name):
        super().__init__(file_name)
        header = "Endpoints\n"
        self.out_result = fpdf.FPDF(format='letter')
        self.out_result.add_page()
        self.out_result.set_font("Arial", size=12)
        self.out_result.cell(200, 10, txt=header, ln=1, align="L")
        self.out_result.set_font("Arial", size=9)

    def add_row(self, row_data):
        result_row = "Endpoint: {name} - {url}, Time: {time} ms, result: {response_code}\n".format(
            name = row_data['name'],
            url = row_data['url'],
            time = row_data['time'],
            response_code = row_data['responseCode']['code']
        )
        self.out_result.cell(200, 10, txt=result_row, ln=1, align="L")

    def __del__(self):
        self.out_result.output(self.file_name)
