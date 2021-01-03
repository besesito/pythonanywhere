from django.shortcuts import render
import operator

def count(request):
    return render(request, 'count/count.html')

def counted(request):
    fulltext = request.GET['fulltext']
    text_list = fulltext.split()
    dictionary={}
    for x in text_list:
        dictionary[x]=text_list.count(x)
    dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count/counted.html', {'fulltext':fulltext, 'total':len(text_list), 'dictionary':dictionary})
