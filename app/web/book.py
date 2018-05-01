from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YushuBook
from . import web


# app.add_url_rule('/hello/',view_func=hello)     #注册路由的第二种方式
@web.route('/book/search/<q>/<page>')     #注册路由的第一种方式
def search():
    '''
    q:关键字 or ISBN号
    '''
    # q = request.args['q']
    # page = request.args['page']

    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip() #strip函数去除字符串前后的空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YushuBook.search_by_isbn(q)
        else:
            result = YushuBook.search_by_keyword(q)
        # return json.dumps(result),200,{'content-type':'application/json'}
        return jsonify(result)
    else:
        return jsonify(form.errors)