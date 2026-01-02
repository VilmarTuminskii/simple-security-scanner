import argparse
from modules.port_scan import port_scan
from modules.http_enum import http_enum
from modules.utils import banner

def main():
    banner()

    parser = argparse.ArgumentParser(
        description="Scanner de Segurança em Python - Uso Educacional (Red Team)"
    )
    parser.add_argument("--target", required=True, help="Alvo (IP ou domínio)")
    parser.add_argument("--ports", default="1-1024", help="Intervalo de portas (ex: 1-1024)")
    parser.add_argument("--threads", type=int, default=100, help="Quantidade de threads")
    args = parser.parse_args()

    print(f"[+] Alvo         : {args.target}")
    print(f"[+] Portas       : {args.ports}")
    print(f"[+] Threads      : {args.threads}\n")

    port_scan(args.target, args.ports, args.threads)
    http_enum(args.target)

if __name__ == "__main__":
    main()
