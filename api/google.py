import gspread
import environ
from pathlib import Path
import os

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

CREDENTIALS = {
    "type": env("type"),
    "project_id": env("project_id"),
    "private_key_id": env("private_key_id"),
    "private_key": env("private_key").replace(r'\n','\n'),
    "client_email": env("client_email"),
    "client_id": env("client_id"),
    "auth_uri": env("auth_uri"),
    "token_uri": env("token_uri"),
    "auth_provider_x509_cert_url": env("auth_provider_x509_cert_url"),
    "client_x509_cert_url": env("client_x509_cert_url")
}

auth = gspread.service_account_from_dict(CREDENTIALS)
doc = auth.open_by_key("1LragT8P41KwjRvdixHr1i5e_XbvytzSH-yHiRckTg6o")

def getSheetScore():
    worksheet = doc.get_worksheet(0)
    team = [i for i in worksheet.col_values(1)[1:]]
    score = [int(i) for i in worksheet.col_values(2)[1:]]
    color = [i for i in worksheet.col_values(3)[1:]]

    parse = [{
        'team' : team[i],
        'score' : score[i],
        'color' : color[i]
    } for i in range(10)]

    return sorted(parse,key=lambda item: item['score'],reverse=True)
    # return [{'team':i['Team'],'score':i['Score'],'color':i['Color']} for i in result]