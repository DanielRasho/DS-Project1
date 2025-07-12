from bs4 import BeautifulSoup
import pandas as pd
import glob

html_files = glob.glob("../src/*.html")

def parse_file(filepath):
    print(f"Start ${filepath}!")
    with open(filepath) as fp:
        
        soup = BeautifulSoup(fp, 'html.parser')

        table = soup.find("table", id="_ctl0_ContentPlaceHolder1_dgResultado")
        rows = table.find_all('tr')
        
        # GET HEADERS
        headersData = rows[0].find_all('td')
        headers = []
        for h in headersData[1:]:
            headers.append(h.get_text())

        # GET DATA
        df = pd.DataFrame(columns=headers)

        for row in rows[1:-1]:
            columns = row.find_all('td')
            cell_values = []
            for cell in columns[1:]:
                cell_values.append(cell.get_text())

            df.loc[len(df)] = cell_values

        print(f"finish with ${filepath}!")
        return df

final_df = pd.concat((parse_file(file) for file in html_files), ignore_index=True)
final_df.to_csv("../data/institutions.csv")