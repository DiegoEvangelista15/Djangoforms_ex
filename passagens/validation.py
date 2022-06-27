def origem_destino_iguais(origem, destino, lista_erros):
    """Verifica se Origem e Destinos sao iguais"""
    if origem  ==  destino:
            lista_erros['destino'] = 'Origem e Destino nao podem ser o mesmo dado!!!'
            
def campo_numero(valor_campo, nome_campo, lista_erros):
    if any(char.isdigit() for char in valor_campo):
            lista_erros[nome_campo] = 'Nao inclua números neste campo!!!'
            
def data_ida_maior_data_volta(data_ida, data_volta, lista_erros):
    if data_ida > data_volta:
        lista_erros['data_volta'] = 'Data de Volta nao pode ser maior que data de volta!!!'
        
def data_ida_menor_hoje(data_ida, data_pesquisa, lista_erros):
    if data_ida < data_pesquisa:
        lista_erros['data_ida'] = 'Data de Ida nao pode ser menor que data de hoje!!!'