class ReportGenerator:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def generate_report(self, top_n_words=10):
        report = (
            f"Word Count: {self.analyzer.get_word_count()}\n"
            f"Sentence Count: {self.analyzer.get_sentence_count()}\n"
            f"Average Word Length: {self.analyzer.get_average_word_length():.2f}\n"
            f"Top {top_n_words} Words:\n"
        )
        top_words = self.analyzer.get_top_words(top_n_words)
        for word, frequency in top_words:
            report += f"{word}: {frequency}\n"
        return report

    def save_report(self, file_path, report):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(report)
            print(f"Report saved to {file_path}")
        except Exception as e:
            print(f"An error occurred while saving the report: {e}")