import requests
from bs4 import BeautifulSoup
import csv

program_data = []

with open('links.txt', 'r') as file:
    for line in file:
        part = line.strip()
        yay = part.split('/')

        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/116.0"
        }
        url = f"https://collegedunia.com{part}"

        response = requests.get(url, headers=headers)


        soup = BeautifulSoup(response.text, "html.parser")

        rows = soup.find_all('tr', class_='jsx-470804739')


        country = yay[1]
        university = yay[3].split('-')
        city = university[len(university) - 1]
        university.remove(city)
        university.remove(university[0])
        university = ' '.join(university)

        for row in rows:
            program = row.find('a', class_='jsx-470804739')
            deadline = row.find('span', class_='jsx-470804739 text-capitalize')
            fees = row.find('span', class_='jsx-470804739 fee-total font-weight-bold text-black')

            scores = row.find_all('span', class_='jsx-470804739 font-weight-bold')
            toefl_score = scores[0].text if len(scores) > 0 else ''
            gre_score = scores[2].text if len(scores) > 2 else ''
            gmat_score = scores[3].text if len(scores) > 3 else ''
            ielts_score = scores[1].text if len(scores) > 1 else ''

            program_data.append({
                'University': university,
                'City': city,
                'Country': country,
                'Program Name': program.text if program else '',
                'Deadline': deadline.text if deadline else '',
                'Fees': fees.text if fees else '',
                'TOEFL Score': toefl_score,
                'GRE Score': gre_score,
                'GMAT Score': gmat_score,
                'IELTS Score': ielts_score,
            })

csv_filename = 'dunia.csv'
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['University', 'City', 'Country', 'Program Name', 'Deadline', 'Fees', 'TOEFL Score', 'GRE Score', 'GMAT Score', 'IELTS Score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    writer.writerows(program_data)

print(f'Data saved to {csv_filename}')