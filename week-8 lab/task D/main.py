from filereader import FileReader
from textanalyzer import TextAnalyzer
from reportgenerator import ReportGenerator

def main():
    file_path = input("Enter the path of the text file to be analyzed: ")
    file_reader = FileReader()
    file_contents = file_reader.read_file(file_path)

    if file_contents:
        text_analyzer = TextAnalyzer(file_contents)
        report_generator = ReportGenerator(text_analyzer)

        report = report_generator.generate_report()

        save_path = input("Enter the path where the report should be saved: ")
        report_generator.save_report(save_path, report)

if __name__ == "__main__":
    main()