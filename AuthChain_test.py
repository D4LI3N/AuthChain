from AuthChain import AuthChain

def registracija(username, password):
    blockchain.register_user('user1', 'password123')
    return "    [*] Registrovan korisnik: " + username

def prijava(username, password):
    return "Prijava uspešna!" if blockchain.login_user(username, password) else "Netočno korisničko ime ili lozinka!"

# Testiranje AuthChain-a
if __name__ == "__main__":

    # Stvaranje nove instance mreže
    blockchain = AuthChain()
    
    # Testni nalozi
    testni_korisnici = [('user1', 'pass1',), ('user2', 'pass2',)]

    # Registracija testnih korisnika
    for k_ime, k_loz in testni_korisnici:
            print("[0]", "Registracija korisnika:",k_ime, k_loz)
            print("[0]", registracija(k_ime, k_loz))

    # 1. Pokušaj prijave sa točnim podatcima
    print("[1]", "Pokušaj prijave sa točnim podatcima:", testni_korisnici[0][0], testni_korisnici[0][1])
    print("[1]", prijava(testni_korisnici[0][0], testni_korisnici[0][1]) )

    # 2. Pokušaj prijave sa netočnom lozinkom
    print("[2]", "Pokušaj prijave sa netočnom lozinkom:", testni_korisnici[0][0], "netočna_lozinka")
    print("[2]", prijava(testni_korisnici[0][0], "netočna_lozinka") )

    # 3. Pokušaj prijave sa ne postojećim korisnikom
    print("[3]", "Pokušaj prijave sa netočnom lozinkom:", "nepostojeći", "netočna_lozinka")
    print("[3]", prijava("nepostojeći", "netočna_lozinka") )