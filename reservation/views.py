from django.shortcuts import render

# Create your views here.
def Table_book(request):
    return render(request,template_name='reservation\Table_book.html')

def Confo_table_book(request):
    return render(request,template_name='reservation\Confo_table_book.html')

def Book_history(request):
    return render(request,template_name='reservation\Book_history.html')



