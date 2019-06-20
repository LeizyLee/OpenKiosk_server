class SyncCursor:
    def __init__(self, _host='202.31.147.28', _user='admin', _password='qwe123!!@@', _db='menu', _charset='utf8'):
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

    def show_table(self):
        print(self.table_list)

    def get_table(self):
        return self.table_list

def seperate_table(_list):
    Positive = []
    Negative = []
    Complexive = []
    Normal = []
    for i in _list:
        if i[-2] == '복합':
            Complexive.append(i)
        elif i[-2] == '중립':
            Normal.append(i)
        elif i[-2] == '긍정':
            Positive.append(i)
        elif i[-2] == '부정':
            Negative.append(i)
    result_list = [Positive, Negative, Normal, Complexive]
    return result_list

def drawing_graph(_list):
    # subplot(221)
    """
    221        222

    223        223
    """
    graph_title = ["Positive", "Negative", "Normal", "Complexive"]
    #(1, '가격이 괜찮았지만 직원이 친절하지 않았다. 생선은 원재료가 맛있으니까 괜찮지만 양이 너무 적다.', '복합', '99%')
    plt_num = 221
    for i in _list:
        plt.subplot(plt_num)
        tx = len(i)
        ty = [int(x[-1][:-1]) for x in i]
        plt.plot(ty)
        plt.axis([0,tx,0,100])
        plt.xlabel('review num')
        plt.ylabel('Correct Percent')
        plt.title(graph_title[plt_num - 221])
        plt_num += 1

    #print(tScore)
    #plt.plot(tScore)
    # plot ( y_데이터 ) or plot(y_데이터, x_데이터)
    # axis(x_start, x_end, y_start, y_end)
    plt.show()


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    Sync = SyncCursor()

    table_list = Sync.get_table()
    drawing_graph(seperate_table(table_list))



