import urllib.request

# URL of the CSV file
csv_url = 'https://raw.githubusercontent.com/prasertcbs/basic-dataset/refs/heads/master/Nobel%20Laureattes.csv'
csv_file_path = 'nobel_laureates.csv'

# Function to download the CSV file
def download_csv_file(url, save_path):
    with urllib.request.urlopen(url) as response, open(save_path, 'wb') as out_file:
        data = response.read()
        out_file.write(data)
    print(f"CSV file downloaded and saved to {save_path}")

# Function to read the CSV file and count Nobel prizes by country
def count_prizes_by_country(csv_path):
    country_names = []
    prize_counts = []

    with open(csv_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        # Skip the header line
        for line in lines[1:]:
            fields = line.split(',')
            birth_country = fields[4].strip().strip('"')

            if birth_country in country_names:
                index = country_names.index(birth_country)
                prize_counts[index] += 1
            else:
                country_names.append(birth_country)
                prize_counts.append(1)

    return country_names, prize_counts

# Function to sort countries by prize counts and get the top 20
def get_top_20_countries(country_names, prize_counts):
    # Bubble sort to sort countries by prize counts
    n = len(prize_counts)
    for i in range(n):
        for j in range(0, n-i-1):
            if prize_counts[j] < prize_counts[j+1]:
                prize_counts[j], prize_counts[j+1] = prize_counts[j+1], prize_counts[j]
                country_names[j], country_names[j+1] = country_names[j+1], country_names[j]

    # Get the top 20 countries
    top_20_countries = country_names[:20]
    top_20_counts = prize_counts[:20]

    return top_20_countries, top_20_counts

# Function to print the top 20 countries with their prize counts
def print_top_20_countries(top_20_countries, top_20_counts):
    print("Top 20 Countries with Most Nobel Prizes:")
    for country, count in zip(top_20_countries, top_20_counts):
        print(f"{country}: {count}")

# Main script execution
if __name__ == "__main__":
    # Step 1: Download and save the CSV file
    download_csv_file(csv_url, csv_file_path)

    # Step 2: Read the CSV file and count Nobel prizes by country
    country_names, prize_counts = count_prizes_by_country(csv_file_path)

    # Step 3: Sort countries by prize counts and get the top 20
    top_20_countries, top_20_counts = get_top_20_countries(country_names, prize_counts)

    # Step 4: Print the top 20 countries with their prize counts
    print_top_20_countries(top_20_countries, top_20_counts)