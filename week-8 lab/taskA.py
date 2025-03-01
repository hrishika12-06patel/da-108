import os

def read_file_content(file_path: str) -> str:
    """
    Reads the content of a file and returns it as a string.
    
    Args:
        file_path (str): The path of the file to read.
        
    Returns:
        str: The content of the file.
        
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file at path {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        content = file.read()
    
    return content

if __name__ == "__main__":
    file_path = input("Enter the path of the file to read: ")
    try:
        content = read_file_content(file_path)
        print("File content:\n", content)
    except FileNotFoundError as e:
        print(e)