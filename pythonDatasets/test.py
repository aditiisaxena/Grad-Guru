import requests
from bs4 import BeautifulSoup
import csv

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"
}
url = "https://collegedunia.com/uk/university/863-university-of-nottingham-nottingham"

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Initialize lists to store extracted data
program_data = []

# Find all the rows in the HTML table (assuming your data is in a table)
rows = soup.find_all('tr', class_='jsx-470804739')

for row in rows:
    program = row.find('a', class_='jsx-470804739 d-block')
    deadline = row.find('span', class_='jsx-470804739 text-capitalize')
    fees = row.find('span', class_='jsx-470804739 fee-total font-weight-bold text-black')

    # Extract TOEFL, GRE, GMAT, and IELTS scores
    scores = row.find_all('span', class_='jsx-470804739 font-weight-bold')
    toefl_score = scores[0].text if len(scores) > 0 else ''
    gre_score = scores[2].text if len(scores) > 2 else ''
    gmat_score = scores[3].text if len(scores) > 3 else ''
    ielts_score = scores[1].text if len(scores) > 1 else ''

    # Append the extracted data to the program_data list
    program_data.append({
        'Program Name': program.text if program else '',
        'Deadline': deadline.text if deadline else '',
        'Fees': fees.text if fees else '',
        'TOEFL Score': toefl_score,
        'GRE Score': gre_score,
        'GMAT Score': gmat_score,
        'IELTS Score': ielts_score,
    })

# Write the extracted data to a CSV file
csv_filename = 'programData.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Program Name', 'Deadline', 'Fees', 'TOEFL Score', 'GRE Score', 'GMAT Score', 'IELTS Score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    # Write the header row
    writer.writeheader()
    
    # Write the program data
    writer.writerows(program_data)

print(f'Data saved to {csv_filename}')
