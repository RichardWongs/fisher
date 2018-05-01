

def is_isbn_or_key(word):
    '''
    判断传入的参数是关键字还是ISBN号,并将判断结果返回
    ISBN13:13位0--9的数字组成
    ISBN10:10个0--9的数字组成,中间包含'-'
    '''
    isbn_or_key = 'key'
    if len(q) == 13 and word.isdigit():
        isbn_or_key == 'isbn'
    short_word = word.replace('-','')
    if '-' in word and len(word) == 10 and short_word.isdigit():
        isbn_or_key == 'isbn'
    return isbn_or_key