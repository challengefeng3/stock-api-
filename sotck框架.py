from tkinter import *
import tkinter.messagebox as messagebox
import urllib.request
import json
import pandas as pd
#要下载pandas库
import numpy as np
#要下载pandas库
import pymssql
#要下载pymssql库


class Application(Frame):      
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='测试股票代码', command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo(processdata)


def get_raw_data(x):
    return json.loads(urllib.request.urlopen(x).read())['result']




###转换可数据分析的dataframe格式
#定义转换dataframe函数
def to_dataframe(x):
    print(x)
#列表分裂
    z=x.split(',')
    print(z)
#数据处理
    df=pd.DataFrame(z,index=['日期','开盘','收盘','最高价','最低价','成交量','振幅'])
    print(df.T)
    return df.T



def connectsql(x):
    #数据库服务器地址/用户名/密码/数据库库名字
    conn = pymssql.connect("challenge","sa","ABCabc1234","stock")
    cursor = conn.cursor()
    #插入数据库数据,数据库表名stock,列名'日期','开盘','收盘','最高价','最低价','成交量','振幅'
    insertSql = "insert into dbo.stock([日期],[开盘],[最高价],[最低价],[成交量],[振幅],) values(%s,'%s','%s','%s','%s','%s','%s')" %(x)
    cur.execute(insertSql)
    # 关闭连接
    conn.close()

    

####提取案例数据网址
url=r'http://stock.liangyee.com/bus-api/stock/freeStockMarketData/getDailyKBar?userKey=3e67269ba0a148ef8aba0bbc906c5143&startDate=2018-03-29&symbol=002037&endDate=2018-03-29&type=1'    
###提取数据
rawdata=get_raw_data(url)
processdata=to_dataframe(rawdata)    
connectsql(processdata)
app = Application()
app.master.title('api测试股票1.0')
app.mainloop()    





















