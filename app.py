import requests
import re
from bs4 import BeautifulSoup as bs
from wordcount import sort
from spider.requests_message import sipder
import json
from flask import Flask, render_template, request

app = Flask(__name__)
spider = sipder()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/getting', methods=['GET', 'POST'])
def getting():
    if request.method == 'POST':
        app = request.form.get('app')
        res = requests.get('https://www.chandashi.com/search/index?keyword={}&type=store&country=cn&from=input&data_type=kw'.format(app))  # 发送请求
        html = res.text
        soup = bs(html, "html.parser")  # 定义一个BeautifulSoup变量
        css_class = soup.find(attrs={'class': 'app-item'})
        css_class = str(css_class)
        appid = re.search('\d{9,10}', css_class).group()
        print(appid)
        if spider.start(appid):
            return render_template('success.html')
    return render_template('getting.html')


@app.route('/show')
def show():
    with open(r'data/test_data.json', 'r') as f:
        data = json.load(f)
    return render_template('show.html', data=data['data'])


@app.route('/wordcount')
def wordcount():
    Data = sort().start()
    print(Data)
    print(type(Data))
    return render_template('wordcount.html', Data=Data)


if __name__ == '__main__':
    app.run(debug=True)
