import csv

company_l = []
company = {}
company_res = []

with open('vacancy.csv', 'r', newline='', encoding='utf-8') as csvf:
    f = csv.DictReader(csvf, delimiter=';', quotechar='|')

    for i in f:
        s = int(i["Salary"])
        if not(i["Company"] in company_l):
            company_l.append(i["Company"])
            company[i["Company"]] = {"summ": 0, "count": 0}
            if s < 45000:
                company[i["Company"]]["summ"] = company[i["Company"]]["summ"] + (s - (s * 0.08))
            elif 45001 < s < 50000:
                company[i["Company"]]["summ"] = company[i["Company"]]["summ"] + (s - (s * 0.1))
            else:
                company[i["Company"]]["summ"] = company[i["Company"]]["summ"] + (s - (s * 0.13))
            company[i["Company"]]["count"] = company[i["Company"]]["count"] + 1
        else:
            if s < 45000:
                company[i["Company"]]["summ"] = company[i["Company"]]["summ"] + (s - (s * 0.08))
            elif 45001 < s < 50000:
                company[i["Company"]]["summ"] = company[i["Company"]]["summ"] + (s - (s * 0.1))
            else:
                company[i["Company"]]["summ"] = company[i["Company"]]["summ"] + (s - (s * 0.13))
            company[i["Company"]]["count"] = company[i["Company"]]["count"] + 1

for j in company_l:
    m = company[j]["summ"] / company[j]["count"]
    company_res.append([j, int(m)])

with open('vacancy_average.txt', 'w+', encoding='utf-8') as file:
    file.write(str(company_res))
