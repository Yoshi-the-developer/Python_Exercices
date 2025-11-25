import requests

def recuperer_posts():
    """Récupère les posts depuis l'API JSONPlaceholder."""
    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url, timeout=5)
    except requests.exceptions.RequestException as e:
        print("Erreur réseau :", e)
        return []

    if response.status_code != 200:
        print("Erreur HTTP :", response.status_code)
        return []

    try:
        posts = response.json()
    except ValueError:
        print("Réponse non valide (JSON).")
        return []

    return posts


def afficher_resume_posts(posts, n=5):
    print(f"\nAperçu des {n} premiers posts :")
    limite = min(n, len(posts))
    for i in range(limite):
        post = posts[i]
        print(f"Post #{post['id']} (user {post['userId']}) : {post['title']}")


if __name__ == "__main__":
    posts = recuperer_posts()
    print("Nombre de posts récupérés :", len(posts))
    if posts:
        afficher_resume_posts(posts, 5)