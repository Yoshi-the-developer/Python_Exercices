notes = [] 

with open('Exo5.txt', 'r', encoding='utf-8') as fichier:
    
    for ligne in fichier:
        
        ligne_nettoyee = ligne.strip()
        
        if ligne_nettoyee:
            
            note = float(ligne_nettoyee)
            
            notes.append(note)

print(f"Liste des notes lues et converties : {notes}")

if notes:
    note_min = min(notes) 
    note_max = max(notes) 
    
    somme_notes = sum(notes)      
    nombre_notes = len(notes)      
    moyenne = somme_notes / nombre_notes
    
    notes_validees = 0
    
    for note in notes:
        if note >= 10:
            notes_validees += 1
            
    # --- Affichage Final des Résultats ---
    print("\n--- Résultats des Statistiques ---")
    print(f"La note minimale est : {note_min}")
    print(f"La note maximale est : {note_max}")
    print(f"La moyenne des notes est : {moyenne:.2f}") #  arrondi à 2 décimales
    print(f"Nombre de notes >= 10 : {notes_validees} sur {nombre_notes}")
else:
    print("Le fichier ne contenait aucune note à traiter.")