import nmap


def alvo():
    ip = str(input('Informe o ip: '))
    nm = nmap.PortScanner()
    nm.scan(ip)
    return nm[ip]['tcp'].keys()
