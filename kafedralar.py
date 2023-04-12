import requests
from bs4 import BeautifulSoup

KAFEDRALAR_URL = "https://omgtu.ru/general_information/the-structure/the-department-of-university.php"


def get_kafedralar():
    page = requests.get(KAFEDRALAR_URL)
    parser = BeautifulSoup(page.text, "html.parser")

    page_content = parser.find('div', id="pagecontent")
    links = page_content.findAll('a')

    kafedralar = []
    for x in links:
        kafedralar.append(x.text)

    return kafedralar


def write_to_file(kafedralar, name='kafedralar.txt'):
    f = open(name, 'w')
    for x in kafedralar:
        print(x, file=f)
    f.close()

    print("Результат в файле", name)
