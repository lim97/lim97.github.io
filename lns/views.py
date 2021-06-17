from django.shortcuts import render


def main(request):
    return render(request,"lns/lns_main.html")