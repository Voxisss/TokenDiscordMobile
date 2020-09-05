# coding: utf-8
import requests
import time
import sys
import subprocess
import os

print("Credit : Voxis")

while True:
    email = str(input("Entrez votre email: "))
    password = str(input("Entrez votre mot de passe: "))

    payload = {     
                "email": email,
                "password": password
              }

    r = requests.post('https://discord.com/api/v8/auth/login', json=payload).json()
    if "captcha_key" in r:
        print("Un captcha est demandé, l'email entré est invalide ou a été tenté à de trop nombreuses reprises à la connexion. Réécrivez vos informations")
        time.sleep(1)
    elif "errors" in r:
        print("Une erreur est survenue. Réécrivez vos informations.")
    elif r["token"] == None:
        break
    else:
        print("-----------TOKEN-----------")
        print("Voici votre token: " + r["token"])
        time.sleep(5)
        sys.exit()

while True:
    if r["token"] == None:
        print("-----------Vérification A2F-----------")
        code = input("Entrez le code d'authentification de l'A2F: ")
        mfa_payload = {
                        "code": code,
                        "ticket": r["ticket"]
                      }
        r2 = requests.post('https://discord.com/api/v8/auth/mfa/totp', json=mfa_payload).json()
        if "message" in r2:
            print("Le code d'authentification A2F est incorrect. Réécrivez le code.")
            time.sleep(1)
        else:
            print("-----------TOKEN-----------")
            print("Voici votre token: " + r2["token"])
            time.sleep(5)
            sys.exit()
