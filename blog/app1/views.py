from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
import MySQLdb



def get_book_list():
    db = MySQLdb.connect(user='root', db='books', passwd='123456', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT book_name FROM books')
    book_list = [row[0] for row in cursor.fetchall()]
    db.close()
    print("=="*10)
    print (book_list)
    print("=="*10)
    return book_list

#return html without request object
def book_list(request):
    book_list = get_book_list()
    #book_list=["Assassin's Creed",'Monster Hunter 5','Neverwinter Nights']
    return render_to_response('app1/book_list.html', {'book_list': book_list})


#return pure string
def index_string(request):
    return HttpResponse("Hello, this is index...")

#return html with request object
def index(request):
    data = "Hello, i'm come from mysql"
    return render(request,'app1/index.html',{'data': data})