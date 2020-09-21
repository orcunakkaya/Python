import requests,sys
from PyQt5.QtGui import QIcon
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *


count = 0
list_movie_name = list()
list_movie_year= list()
list_movie_runtime = list()
list_movie_genre = list()
list_movie_rating = list()

class Top250():
    def __init__(self,url):
        self.url = url
        self.response = requests.get(self.url)
        self.html_content = self.response.content
        self.soup = BeautifulSoup(self.html_content, "html.parser")
        self.movie_Names()
        self.movie_Year()
        self.movie_Runtime()
        self.movie_Genre()
        self.movie_Rating()


    def movie_Names(self):
        movie_names = self.soup.find_all('h3', class_='lister-item-header')

        for name in movie_names:
            list_movie_name.append(name.find('a').text)

    def movie_Year(self):
        global count
        movie_year = self.soup.find_all('h3', class_='lister-item-header')
        for year in movie_year:

            yr = year.find('span',class_='lister-item-year text-muted unbold').text
            if (count == 59):
                yr = yr[4:9]
            if (count == 176 or count == 181 or count == 183 or count==185):
                yr = yr[5:9]
            else:
                yr = yr[1:5]

            list_movie_year.append(yr)
            count = count +1


    def movie_Runtime(self):
        movie_runtime = self.soup.find_all('p', class_='text-muted')
        temp = list()
        for runtime in movie_runtime:
            temp.append(runtime.find('span',class_='runtime'))
        for i in range(0,len(temp),2):
            list_movie_runtime.append(temp[i].text)


    def movie_Genre(self):
        temp = list()
        movie_genre = self.soup.find_all('p', class_='text-muted')
        for genre in movie_genre:
            temp.append(genre.find('span', class_='genre'))

        for i in range(0,len(temp),2):
            tmp = temp[i]
            list_movie_genre.append(tmp.text.strip())


    def movie_Rating(self):
        movie_rating = self.soup.find_all('div', class_='inline-block ratings-imdb-rating')
        for rating in movie_rating:
            list_movie_rating.append(rating.find('strong').get_text())

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.table_widget = QTableWidget()

        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.table_widget)
        self.setLayout(self.h_box)

        self.table_widget.setRowCount(250)
        self.table_widget.setColumnCount(6)

        self.table_widget.setHorizontalHeaderLabels(["Rank", "Name","Year","Genre","Runtime","Rating"])
        self.table_widget.verticalHeader().setVisible(False)



        for i in range(0,250):
            self.table_widget.setItem(i, 0, QTableWidgetItem(str(i+1)))
            self.table_widget.setItem(i, 1, QTableWidgetItem(str(list_movie_name[i])))
            self.table_widget.setItem(i, 2, QTableWidgetItem(str(list_movie_year[i])))
            self.table_widget.setItem(i, 3, QTableWidgetItem(str(list_movie_genre[i])))
            self.table_widget.setItem(i, 4, QTableWidgetItem(str(list_movie_runtime[i])))
            self.table_widget.setItem(i, 5, QTableWidgetItem(str(list_movie_rating[i])))

        self.setWindowTitle("IMDb TOP 250")
        self.setGeometry(250, 300, 792, 420)
        self.setWindowIcon(QIcon("imdb_icon.png"))


        self.show()



page_1 = Top250("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating")
page_2 = Top250("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt")
page_3 = Top250("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt")
page_4 = Top250("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt")
page_5 = Top250("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=201&ref_=adv_nxt")


app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())