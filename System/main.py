from http.server import HTTPServer, SimpleHTTPRequestHandler

porta = 5432 #pode mudar a porta caso queira
ip = "SEU_IP" #Ip da sua maquina ou Tailscale para acesso remoto
servidor = HTTPServer(("0.0.0.0", porta), SimpleHTTPRequestHandler)

print(f"Servidor: http://{ip}:{porta}")
servidor.serve_forever()