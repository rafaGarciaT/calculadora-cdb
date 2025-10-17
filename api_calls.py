import pandas as pd
import json
import requests


def get_cdi(day, month, year):
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados"
    params = {
        "formato": "json",
        "dataInicial": f"{day - 1}/{month}/{year}",
        "dataFinal": f"{day}/{month}/{year}"
    }

    response = requests.get(url, params=params)
    data = response.json()

    df = pd.DataFrame(data)
    df["valor"] = df["valor"].astype(float)
    valor = df["valor"].astype(float)
    print(df.head())
    return valor[0].astype(float)


def get_ipca(day, month, year):
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados"
    params = {
        "formato": "json",
        "dataInicial": f"01/01/{year}",
        "dataFinal": f"{day}/{month}/{year}"
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data)
    df["valor"] = df["valor"].astype(float)
    print(df.head())
    df["data"] = pd.to_datetime(df["data"], dayfirst=True)
    return df
