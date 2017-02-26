#coding:utf-8
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        tree_h = request.POST.get('tree_h',None)
        if tree_h:
            tree_str = ""
            leaves = 1
            tree_h = int (tree_h)
            for i in range(tree_h):
                tree_str += ' ' * (tree_h - i) + '*' * leaves + '\n'
                leaves +=2
            for i in range(tree_h):
                tree_str += ' ' * tree_h + '*' + '\n'
            return render(request,"index.html",{"tree_str":tree_str})
    else :
        return render(request,"index.html",{"tree_str":""})

