
import requests 
import sys 
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Jok3r Cyber Security")
print (ascii_banner)

subdomain_listesi = open("sd.txt").read() 
subdomainler = subdomain_listesi.splitlines()

for sub in subdomainler:
    sub_domain_tarama = f"http://{sub}.{sys.argv[1]}" 

    try:
        requests.get(sub_domain_tarama)
    
    except requests.ConnectionError: 
        pass
    
    else:
        print("Valid domain: ",sub_domain_tarama)

			#C*#
#subdomain.py ile sd.txt dosyası aynı dizinde bulunmak zorundadır.

#Örnek kullanım : python3 subdomain.py HEDEFSİTE.COM veya IP ADRESİ.

#sd.txt = subdomain listesinin bulunduğu metin belgesi.

#sd.txt dosyasının içeriğini hedef ve amacınıza göre istediğiniz gibi değiştirebilirsiniz...

#Jok3r
