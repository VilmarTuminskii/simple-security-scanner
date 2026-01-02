import socket
import threading
from queue import Queue

def capturar_banner(ip, porta):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, porta))
        sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
        banner = sock.recv(1024).decode(errors="ignore").strip()
        sock.close()
        return banner
    except:
        return None

def worker(fila, alvo):
    while not fila.empty():
        porta = fila.get()
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            resultado = sock.connect_ex((alvo, porta))

            if resultado == 0:
                banner = capturar_banner(alvo, porta)
                print(f"[ABERTA] Porta {porta}")
                if banner:
                    print(f"         Banner: {banner[:80]}")
            sock.close()
        except:
            pass
        fila.task_done()

def port_scan(alvo, intervalo_portas, threads):
    print("[*] Iniciando varredura de portas...\n")

    inicio, fim = map(int, intervalo_portas.split("-"))
    fila = Queue()

    for porta in range(inicio, fim + 1):
        fila.put(porta)

    for _ in range(threads):
        t = threading.Thread(target=worker, args=(fila, alvo))
        t.daemon = True
        t.start()

    fila.join()
    print("\n[*] Varredura de portas finalizada.\n")
