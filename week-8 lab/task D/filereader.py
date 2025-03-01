class FileReader:
    def read_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: The file at {file_path} was not found.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
