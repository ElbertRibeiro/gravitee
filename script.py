import requests
import yaml

gravitee_base_url = "http://seu-gravitee-instance.com/management"

# Carregue os dados da API a partir do arquivo YAML
caminho_para_arquivo_api = "caminho-para-arquivo-api.yml"

with open(caminho_para_arquivo_api, 'r') as file:
    api_data = yaml.safe_load(file)

# Construa a URL para verificar se a API já existe
api_name = api_data["name"]
api_version = api_data["version"]
api_existence_check_url = f"{gravitee_base_url}/apis/{api_name}/{api_version}"

# Faça a solicitação GET para verificar a existência da API
response = requests.get(api_existence_check_url)

# Verifique se a API já existe
if response.status_code == 200:
    # API já existe, exiba uma mensagem de erro
    print(f"A API '{api_name}' versão '{api_version}' já existe. Não é possível cadastrar novamente.")
    exit(1)
elif response.status_code != 404:
    # Outro código de status, algo deu errado na solicitação
    print(f"Erro ao verificar a existência da API. Código de status: {response.status_code}")
    exit(1)

# Se a API não existe, crie-a
create_api_url = f"{gravitee_base_url}/apis"
create_api_response = requests.post(create_api_url, json=api_data)

# Verifique se a criação foi bem-sucedida
if create_api_response.status_code == 201:
    print(f"API '{api_name}' versão '{api_version}' criada com sucesso.")
else:
    print(f"Erro ao criar a API. Código de status: {create_api_response.status_code}")
    exit(1)
