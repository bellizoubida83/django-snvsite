from django.shortcuts import render


from .models import Documentation

# Create your views here.


def doc_list(request):
    doc_list=Documentation.objects.all()
    print(doc_list)
    context ={'doc': doc_list}
    return render(request,'documentation/doc_list.html', context)

def doc_detail(request,id):
        pass
