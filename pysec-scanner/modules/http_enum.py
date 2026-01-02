import requests

HEADERS_SEGURANCA = [
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Content-Security-Policy",
    "Strict-Transport-Security"
]

def http_enum(alvo):
    print("[*] Iniciando enumeração HTTP...\n")

    if not alvo.startswith("http"):
        url = f"http://{alvo}"
    else:
        url = alvo

    try:
        resposta = requests.get(url, timeout=5)

        print(f"[+] Status HTTP: {resposta.status_code}\n")
        print("[+] Headers HTTP:\n")

        for h, v in resposta.headers.items():
            print(f"{h}: {v}")

        print("\n[!] Análise de Headers de Segurança:\n")
        for header in HEADERS_SEGURANCA:
            if header not in resposta.headers:
                print(f"[-] Header de segurança ausente: {header}")
            else:
                print(f"[+] {header} presente")

    except requests.exceptions.RequestException:
        print("[-] Serviço HTTP não detectado ou inacessível.")

    print("\n[*] Enumeração HTTP finalizada.\n")
