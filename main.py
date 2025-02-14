import sys
from lib.parse_report import ParseReport
from lib.csv_result_file import CsvResultFile
from lib.pdf_result_file import PdfResultFile

def main(file_type, file_name, result_file_name):
    report = ParseReport(file_name)

    match file_type:
        case "csv":
            result_file = CsvResultFile(result_file_name)
        case "pdf":
            result_file = PdfResultFile(result_file_name)
        case _:
            raise Exception("File type is wrong")

    report.read_file(result_file)

if __name__ == '__main__':
    file_type = sys.argv[1]
    file_name = sys.argv[2]
    result_file_name = sys.argv[3]
    main(file_type, file_name, result_file_name)
