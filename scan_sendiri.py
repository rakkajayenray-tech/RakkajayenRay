import socket
print("=== SCAN CIKAMPEK V1 ===")
# Cek port HP sendiri aja!
for port in [22, 80, 443, 8080]:
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect(("127.0.0.1", port))
        print(f"Port {port} = BUKA")
    except:
        print(f"Port {port} = TUTUP - AMAN")
    s.close() 
