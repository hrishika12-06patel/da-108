import os

class FileManager:
    def __init__(self, file_path: str):
        """
        Initializes the FileManager with a file path.
        
        Args:
            file_path (str): The path of the file to manage.
        """
        self.file_path = file_path
    
    def read_contents(self) -> str:
        """
        Reads the contents of the file and returns them as a string.
        
        Returns:
            str: The content of the file.
            
        Raises:
            FileNotFoundError: If the file does not exist.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file at path {self.file_path} does not exist.")
        
        with open(self.file_path, 'r') as file:
            content = file.read()
        
        return content
    
    def write_contents(self, new_contents: str):
        """
        Overwrites the contents of the file with the provided new_contents string.
        
        Args:
            new_contents (str): The new contents to write to the file.
        """
        with open(self.file_path, 'w') as file:
            file.write(new_contents)
    
    def append_contents(self, new_contents: str):
        """
        Appends the new_contents string to the existing contents of the file.
        
        Args:
            new_contents (str): The new contents to append to the file.
        """
        with open(self.file_path, 'a') as file:
            file.write(new_contents)

def main():
    file_path = "example.txt"
    
    # Create a FileManager instance
    file_manager = FileManager(file_path)
    
    # Write new contents to the file
    file_manager.write_contents("Hello, this is a test file.")
    
    # Read and print the contents of the file
    print("File contents after write:")
    print(file_manager.read_contents())
    
    # Append new contents to the file
    file_manager.append_contents("\nThis is an appended line.")
    
    # Read and print the contents of the file
    print("File contents after append:")
    print(file_manager.read_contents())

if __name__ == "__main__":
    main()