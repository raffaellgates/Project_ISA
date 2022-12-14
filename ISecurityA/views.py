from django.shortcuts import render
from django.shortcuts import redirect
from .google_hacking import analisar
from .models import DadosSensiveis, Search
from .forms import SearchForm


def search(request):
    form = SearchForm()
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            obj = is_sgbd(post.url)
            return redirect('ISecurityA:dados_sensiveis', pk=obj.id)
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})


def is_sgbd(link):
    url = Search.objects.filter(url=link).exists()
    if url:
        return Search.objects.get(url=link)
    else:
        analisar(link)
        is_sgbd(link)


def dados_sensiveis(request, pk):
    dados_sensiveis_list = DadosSensiveis.objects.filter(
        url_primary_id=pk,
        tipo_vulnerabilidade=1
        )
    xss = DadosSensiveis.objects.filter(
        url_primary_id=pk,
        tipo_vulnerabilidade=2)
    sql = DadosSensiveis.objects.filter(
        url_primary_id=pk,
        tipo_vulnerabilidade=3)
    docs = DadosSensiveis.objects.filter(
        url_primary_id=pk,
        tipo_vulnerabilidade=4)
    context = {
        'dados_sensiveis_list': dados_sensiveis_list,
        'xss_list': xss,
        'sql_list': sql,
        'docs_list': docs}
    return render(request, 'dados_sensiveis.html', context)
