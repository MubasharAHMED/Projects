print("Bonjour, ce programme permet de coder/décoder un texte") 
Partie="oui"	
while Partie=="oui":
	question=input('Voulez vous crypter un texte ou le decrypter?')
	
	M=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	L=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] #liste de l'alphabet
	E=[" "] #liste pour l"espace
	G=["-",",",".","?","!",":",]
	#début du programme, cas du cryptage
	if question in ["crypter","CRYPTER","Crypté","crypté","crypte"]:
		REP=input('Donnez un mot que vous voulez le crypté:')             #on demande un mot à l'utilisateur
		rep=list(REP)                                                    #On transforme le mot saisie par l'utilisateur en une liste
		taille=len(REP)         #On cherche la taille du mot saisie par l'utilisateur en une liste
		REPONSE=[]    
		#la boucle parcourt chaques lettres du mot et pour chaques lettres elle remplace par la lettre suivante 

		                            
		for k in range (0,taille):                  ## substitue les letttres de "a" à "y" 

			#cas des minuscules	
			for n in range(0,25):
				if rep[k]==L[n]:
					REPONSE.append(L[n+1])
					#print(L[n+1])               #sert a controler
			if rep[k]==L[25]:               ## substitue la letttre de "z"
				#print(L[0])
				REPONSE.append(L[0])
			if rep[k]==E[0]:               ## rajoute l'espace
				#print(E[0])
				REPONSE.append(E[0])

			#cas des ponctuations	
			for n in range(0,3):	
				if rep[k]==G[n]:
					REPONSE.append(G[n])	

			#cas des majuscules	
			for o in range(0,25):
				if rep[k]==M[o]:
					REPONSE.append(M[o+1])
			if rep[k]==M[25]:               
				#print(M[0])
				REPONSE.append(M[0])
			if rep[k]==E[0]:
				#print(E[0])
				REPONSE.append(E[0])	

			#if rep not in M and L and E and G:
			#	print ("veuillez écrire correctement votre mot")


		print ("Le mot crypté de",REP," est","".join(REPONSE)) # join REPONSE permet de transformer la liste REPONSEE en une chaine de caractère (mot ou phrase)

	#cas du décryptage
	if question in["decrypter","DECRYPTER","décrypté","decrypté","décrypte","decrypte"]:
		REP=input('Donnez un mot que vous voulez le décrypté:')             #on demande un mot à l'utilisateur
		rep=list(REP)                                                    #On transforme le mot saisie par l'utilisateur en une liste
		taille=len(REP)
		REPONSE=[] 

		
		for k in range (0,taille):                      ## substitue les letttres de "a" à "y" *

			#cas des minuscules
			for n in range(0,25):
				if rep[k]==L[n]:
					REPONSE.append(L[n-1])
					#print(L[n-1]           #sert a controler
			if rep[k]==L[25]:                 ## substitue la letttre "z"
				#print(L[0])
				REPONSE.append(L[0])
			if rep[k]==E[0]:                ## rajoute l'espace
				#print(E[0])
				REPONSE.append(E[0]) 

			#cas des ponctuations	
			for n in range(0,3):	
				if rep[k]==G[n]:
					REPONSE.append(G[n])	

			#cas des majuscules	
			for o in range(0,25):
				if rep[k]==M[o]:
					REPONSE.append(M[o-1])
			if rep[k]==M[25]:               
				#print(M[0])
				REPONSE.append(M[0])
			if rep[k]==E[0]:
				#print(E[0])
				REPONSE.append(E[0])

		#print(REPONSE) sert à vérifier
		print ("Le mot crypté de",REP," est","".join(REPONSE))
	Partie=input("Voulez vous recommencer, répondez par oui ou non")
