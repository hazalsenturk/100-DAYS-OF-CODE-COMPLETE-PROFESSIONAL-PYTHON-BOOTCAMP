from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

records = []

for i in range(1, 35):

    if i == 1:
        response = requests.get("https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")

    else:
        response = requests.get(f"https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/{i}")

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select("table.data-table tbody tr")
    # for row in rows:
    #     cells = row.select("span.data-table__value")
    #     record = {
    #         "Undergraduate Major": cells[1].getText(),
    #         "Starting Median Salary": float(cells[3].getText().strip("$").replace(",", "")),
    #         "Mid-Career Median Salary": float(cells[4].getText().strip("$").replace(",", "")),
    #     }
    #     records.append(record)
#print(records)
#
# df = pd.DataFrame(records).dropna()
#
# top_fifty = df.sort_values("Starting Median Salary", ascending=False).iloc[0:50]
# print(top_fifty)
#
# plt.subplot(2,1,1)
# salary_variation = top_fifty["Mid-Career Median Salary"].subtract(top_fifty["Starting Median Salary"])
# plt.xlabel("Variation of Salaries ")
# plt.ylabel("Starting Median Salary(SMS)")
# plt.plot(top_fifty["Starting Median Salary"], salary_variation, "bo")
#
# plt.subplot(2,1,2)
# plt.xlabel("Mid-Career Median Salary(MMS)")
# plt.ylabel("Starting Median Salary(SMS)")
# plt.plot(top_fifty["Starting Median Salary"], top_fifty["Mid-Career Median Salary"], "bo")
#
# plt.show()







