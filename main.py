import requests 
import pandas as pd
def requestApiBcb(data):
    """
    função para estrair od dados dos meios de pagamento trimestrais do Banco Central
    parametros:
    data - string - aaaat (Exemplo: 20191)
    """
    url=f"https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosdePagamentosTrimestralDA(trimestre=@trimestre)?@trimestre='{data}'&$format=json"
    req=requests.get(url)
    dados=req.json()
    df=pd.json_normalize(dados['value'])
    return print(df)

requestApiBcb('20241')

