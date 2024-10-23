import requests

def localizarIP(ip):
    api_token = "942ade25"
    url = f"https://api.hgbrasil.com/geoip?format=json-cors&fields=only_results,city,region,country_name&key={api_token}&address={ip}&precision=false"
    
    r = requests.get(url)

    if(r.status_code == 200):
        dados = r.json()
        print(
            f'\n'
            f'Cidade: {dados["city"]} \n'
            f'Estado: {dados["region"]} \n'
            f'País: {dados["country_name"]} \n'
        )
    else:
        
        if(r.status_code >= 400) and (r.status_code <= 499):
            print(f'{r.status_code} - Error related with client error responses')
        elif(r.status_code >= 500) and (r.status_code <= 599):
            print(f'{r.status_code} - Error related with server error responses')
        else:
            print(f'Error: {r.status_code}')


ip_client = input("Digite o IP que quer pesquisar:")

try:
    localizarIP(ip_client)
except:
    print(
        f'Something is wrong with this IP. \n'
        f'Please insert an IP valid.'
        )