#!/usr/bin/python3
# -*- coding: utf-8 -*
"""Lecture de l'image passe en parametre """
choixTicketEssence = ""
import os
import shutil
import platform
from PIL import Image
print("lecture des images dans le répertoire courant")
folder_path = "./images/"
folder_new = "./new_images/"


def function_resizeImage(filename):
	image = Image.open(filename)
	length, width = image.size
	length = length / 2
	width = width / 2
	print(length)
	print(width)
	image = image.resize((int(length), int(width)), Image.ANTIALIAS)
	image.save(filename)
	return;

def function_openFolder(path):
    if platform.system() == "Windows":
        os.startfile("C:/"+ path)

def function_essence(filename):
	"""Fonction pour le renommage des fichiers essence"""
	print("Ticket essence")
	extension = funtion_getExtension(filename)
	montant = input("Saisir le montant de l'opération : ")
	newFilename = "[DEPLACEMENT]["+ montant +"][CARBURANT]"+extension
	shutil.move(folder_path + filename, folder_new + newFilename)
	function_resizeImage(folder_new + newFilename)
	
	return;
	
def function_restauration(filename):
	"""Fonction pour le renommage des fichiers essence"""
	print("Ticket de caisse")
	extension = funtion_getExtension(filename)
	montant = input("Saisir le montant de l'opération : ")
	newFilename = "[RESTAURATION]["+ montant +"]"+extension
	shutil.move(folder_path + filename, folder_new + newFilename)
	function_resizeImage(folder_new + newFilename)
	
	return;

def function_kilometrage(filename):
	"""Fonction pour le renommage des fichiers kilometrage"""
	print("Kilométrage")
	extension = funtion_getExtension(filename)
	km = input("Saisir le kilometrage du véhicule : ")
	newFilename = "[KM]["+ km +"]"+extension
	shutil.move(folder_path + filename, folder_new + newFilename)
	function_resizeImage(folder_new + newFilename)
	
	return;

def funtion_getExtension(filename):
	"""Fonction pour la récupération de l'extension du fichier"""
	filename, file_extension = os.path.splitext(filename)
	return file_extension;

for path, dirs, files in os.walk(folder_path):
	for filename in files:
		"""Pour chaque image demander le traitement à faire"""
		print(filename)
		print("Type image :")
		print("1- Ticket carburant")
		print("2- Kilométrage véhicule")
		print("3- Restauration")
		print("4- Rien")
		choix = input("Saisir choix:")
		print(choix)
		if choix=="1":
			function_essence(filename)
		elif choix == "2":
			function_kilometrage(filename)
		elif choix == "3":
			function_restauration(filename)
		elif choix == "4":
			quit()
