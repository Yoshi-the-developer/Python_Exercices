notes = [12, 5.5, 17, 9, 13, 8, 10]

def calculer_moyenne(notes: list[float]):
    return sum(notes) / len(notes)

def filtrer_notes_suffisantes(notes: list[float], seuil: int):
    result = []
    for n in notes:
        if n >= seuil:
            result.append(n)
    return result

def formater_message(nom: str, moyenne: float):
    return f"Étudiant {nom} : moyenne = {moyenne:.2f}"