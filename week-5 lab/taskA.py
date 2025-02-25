import os
import csv
import urllib.request

# URL of the CSV file
csv_url = 'https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/Country_Flags.csv'
csv_file_path = 'Country_Flags.csv'
flags_directory = 'flags'

# Function to download the CSV file
def download_csv_file(url, save_path):
    with urllib.request.urlopen(url) as response, open(save_path, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
    print(f"CSV file downloaded and saved to {save_path}")

# Function to download and save flag images
def download_flag_images(csv_path, save_directory):
    # Create the flags directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    # Read the CSV file
    with open(csv_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            country_name = row['Country']
            flag_url = row['Flag']
            
            # Download the flag image
            try:
                with urllib.request.urlopen(flag_url) as response:
                    flag_image_path = os.path.join(save_directory, f"{country_name}.png")
                    with open(flag_image_path, 'wb') as out_file:
                        out_file.write(response.read())
                print(f"Downloaded and saved flag for {country_name}")
            except Exception as e:
                print(f"Failed to download flag for {country_name}: {e}")

# Main script execution
if __name__ == "__main__":
    # Step 1: Download and save the CSV file
    download_csv_file(csv_url, csv_file_path)
    
    # Step 2: Read the CSV file and download flag images
    download_flag_images(csv_file_path, flags_directory)