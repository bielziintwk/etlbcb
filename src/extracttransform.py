import requests 
import pandas as pd
"""função -> nome da função"""
def requestApiBcb(data: str)-> pd.DataFrame:
    """
    função para estrair od dados dos meios de pagamento trimestrais do Banco Central
    parametros:
    data - string - aaaat (Exemplo: 20191)

    saida:
    DataFrame - Estrutura de dados do pandas
    """
    url=f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='{data}'&$format=json"
    req=requests.get(url)
    dados=req.json()
    df=pd.json_normalize(dados['value'])
    df = pd.json_normalize(data[""])
    return df

dadosBcb=requestApiBcb('20241')
print(dadosBcb.info())
