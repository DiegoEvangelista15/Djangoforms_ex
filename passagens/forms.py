from django import forms
from tempus_dominus.widgets import DatePicker
from datetime import datetime
from .classe_viagem import tipos_de_classes
from .validation import *
from passagens.models import ClasseViagem, Passagem, Pessoa

# adicionando pelo ModelForm


class PassagensForms(forms.ModelForm):
    # colocando ele fica a frente e modifica
    data_pesquisa = forms.DateField(
        label='Data da Pesquisa', disabled=True, initial=datetime.today())

    class Meta:
        model = Passagem
        # fields = ['origem'] se quiser chamar campo por campo, mas eh horrivel
        fields = '__all__'
        labels = {
            'data_ida': 'Data de Ida',
            'data_volta': 'Data de Volta',
            'informacoes': 'Informações',
        }
        widgets = {
            'data_ida': DatePicker(),
            'data_volta': DatePicker(),
        }


# class PassagensForms(forms.Form):
#     origem = forms.CharField(label='Origem', max_length=100)
#     destino = forms.CharField(label='Destino', max_length=100)
#     data_ida = forms.DateField(label='Ida', widget=DatePicker())
#     data_volta = forms.DateField(label='Volta', widget=DatePicker())
#     data_pesquisa = forms.DateField(label='Data da Pesquisa', disabled=True, initial=datetime.today())
#     classe_viagem = forms.ChoiceField(label='Tipo de Classe do Voo', choices=tipos_de_classes)
#     informacoes = forms.CharField(
#         label='Informações Extras: ',
#         max_length=200,
#         widget=forms.Textarea(),
#         required=False
#     )
#     email = forms.EmailField(label='E-mail:', max_length=150, required=False)

    # def clean_origem(self):  # isso eh uma forma mas nao eh muito boa para diversos tipos de dados
    #     origem = self.cleaned_data.get('origem')

    #     if any(char.isdigit() for char in origem):
    #         raise forms.ValidationError('Origem invalida: nao inclua números!!!')
    #     else:
    #         return origem


    def clean(self):
        origem = self.cleaned_data.get('origem')
        destino = self.cleaned_data.get('destino')
        data_ida = self.cleaned_data.get('data_ida')
        data_volta = self.cleaned_data.get('data_volta')
        data_pesquisa = self.cleaned_data.get('data_pesquisa')
        lista_erros = {}
        campo_numero(origem, 'origem', lista_erros)
        campo_numero(destino, 'destino', lista_erros)
        origem_destino_iguais(origem, destino, lista_erros)
        data_ida_maior_data_volta(data_ida, data_volta, lista_erros)
        data_ida_menor_hoje(data_ida, data_pesquisa, lista_erros)
        if lista_erros is not None:
            for erro in lista_erros:
                mensagem_erro = lista_erros[erro]
                self.add_error(erro, mensagem_erro)

        return self.cleaned_data


class PessoaForms(forms.ModelForm):
    class Meta:
        model = Pessoa
        # vai trazer todos os campos menos o que eu especifiquei
        exclude = ['nome']
        
