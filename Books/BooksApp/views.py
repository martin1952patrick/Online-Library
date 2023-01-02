from django.shortcuts import render

# routes 
# from flask import render_template
# from . import main
# from ..request import get_news, get_sources, get_kenya_news


# @main.route("/")
def index(request):
    return render(request, "BooksApp/index.html")
    # sources = get_sources()
    # news = get_news()
    # kenya = get_kenya_news()
    
    # , sources = sources, news = news, kenya = kenya)

# @main.route("/news")
# def news():
#     news = get_news()
#     kenya = get_kenya_news()
#     return render_template("news.html", news = news, kenya = kenya)

# @main.route("/about")
# def about():
#     return render_template("about.html")
