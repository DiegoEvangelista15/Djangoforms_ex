from django.shortcuts import render
from passagens.forms import PassagensForms, PessoaForms

# Create your views here.


def index(request):
    form = PassagensForms()
    pessoa_form = PessoaForms(request.POST)
    contexto = {'form': form, 'pessoa_form': pessoa_form}
    return render(request, 'index.html', contexto)


def revisao_consulta(request):
    if request.method == 'POST':
        form = PassagensForms(request.POST)
        pessoa_form = PessoaForms(request.POST)
        if form.is_valid():
            contexto = {'form': form, 'pessoa_form': pessoa_form}
            return render(request, 'minha_consulta.html', contexto)
        else:
            contexto = {'form': form}
            return render(request, 'index.html', contexto)
