from django.shortcuts import render
import operator

def count(request):
    return render(request, 'count/count.html')

def counted(request):
    text = request.POST
    try:
        text2 = text.__getitem__('fulltext')
        text_list = text2.split()
        dictionary = {}
        for x in text_list:
            dictionary[x] = text_list.count(x)
        dictionary = sorted(dictionary.items(), key=operator.itemgetter(1), reverse=True)
        return render(request, 'count/counted.html', {'total': len(text_list), 'dictionary': dictionary})
    except:
        return render(request, 'count/counted.html')
