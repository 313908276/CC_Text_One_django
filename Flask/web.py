from flask import Flask,render_template

app=Flask(__name__)

# 创建了网址/show/info 和 函数index 的对应关系
# 以后用户在浏览器输入网址/show/info 时，就会执行index函数
@app.route("/show/info")
def index():
    # return "中国联通"
    # 默认：去当前项目目录的template文件夹中找
    return render_template("index.html")
@app.route("/get/news")
def get_News():
    return render_template("news.html")

if __name__ == '__main__':
    app.run()