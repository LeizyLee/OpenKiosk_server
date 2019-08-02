class SyncCursor:
    def __init__(self, _host='192.168.25.4', _user='master', _password='qwe123!!@@', _db='menu', _charset='utf8'):
        try:
            import pymysql

            self.conn = pymysql.connect(host=_host, user=_user, password=_password, db=_db, charset=_charset)
            self.cur = self.conn.cursor()
            sql = "select * from menu.review"
            self.cur.execute(sql)
            self.table_list = list(self.cur.fetchall())
        except ImportError as e:
            print(e)
            exit()
        import matplotlib.pyplot
        self.plt = matplotlib.pyplot

        self.Positive = []
        self.Negative = []
        self.Complexive = []
        self.Normal = []

        self.sepTable()

        sql = "select * from menu.menulist"
        self.cur.execute(sql)
        self.menu_list = list(self.cur.fetchall())

        sql = "SELECT s.salesId, s.date, m.idmenulist, m.name, m.price " \
              "FROM salesstatics as s " \
              "INNER JOIN menulist as m " \
              "ON s.id_num = m.idmenulist;"
        self.cur.execute(sql)
        self.sales_list = list(self.cur.fetchall())

    def show_table(self):
        print(self.table_list)

    def get_table(self):
        return self.table_list

    def sepTable(self):
        for i in self.table_list:
            if i[-2] == '복합':
                self.Complexive.append(i)
            elif i[-2] == '중립':
                self.Normal.append(i)
            elif i[-2] == '긍정':
                self.Positive.append(i)
            elif i[-2] == '부정':
                self.Negative.append(i)

    def showSepGraph(self, option=0):
        graph_title = ["Positive", "Negative", "Normal", "Complexive"]
        tempdir = []
        if option == 0:
            tempdir = self.Positive.copy()
        elif option == 1:
            tempdir = self.Negative.copy()
        elif option == 2:
            tempdir = self.Normal.copy()
        elif option == 3:
            tempdir = self.Complexive.copy()

        temp = self.plt
        tx = len(tempdir)
        ty = [int(x[-1][:-1]) for x in tempdir]
        temp.plot(ty)
        temp.grid(b=True, which='both', axis='both')
        #temp.tight_layout()
        temp.axis([0, tx, 0, 100])
        temp.xlabel('review num')
        temp.ylabel('Correct Percent')
        temp.title(graph_title[option])
        temp.savefig("foo.png", dpi=400)
        temp.close()
        #temp.show()
        del temp

    def showAllGraph(self):
        # subplot(221)
        """
        221        222

        223        223
        """
        graph_title = ["Positive", "Negative", "Normal", "Complexive"]
        temp_list = [self.Positive, self.Negative, self.Normal, self.Complexive]
        temp = self.plt

        plt_num = 221
        for i in temp_list:
            temp.subplot(plt_num)
            tx = len(i)
            ty = [int(x[-1][:-1]) for x in i]
            temp.plot(ty)
            temp.grid(b=True, which='both', axis='both')
            temp.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
            temp.axis([0, tx, 0, 100])
            temp.xlabel('review num')
            temp.ylabel('Correct Percent')
            temp.title(graph_title[plt_num - 221])
            plt_num += 1
            temp.savefig("foo.png", dpi=100)
        #temp.show()
        temp.close()
        del temp

if __name__ == "__main__":
    Sync = SyncCursor()
    print("sales_list")
    print(Sync.sales_list[0])
    print("menu_list")
    print(Sync.menu_list[0])
    print("table_list")
    print(Sync.table_list[0])
    temp = [i for i in Sync.sales_list if i[2] == 1001]
    print(temp)
    #Sync.showSepGraph(2)
    #Sync.showAllGraph()
    #table_list = Sync.get_table()
    #drawing_graph(seperate_table(table_list))



