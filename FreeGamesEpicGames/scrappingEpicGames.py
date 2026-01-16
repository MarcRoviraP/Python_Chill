import webbrowser
import requests

url = "https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions"
params = {
    "locale": "es-ES",
    "country": "ES",
    "allowCountries": "ES"
}

data = requests.get(url, params=params).json()
games = data["data"]["Catalog"]["searchStore"]["elements"]

free_games = []

for game in games:
    if not (game.get("promotions") and game["price"]["totalPrice"]["discountPrice"] == 0):
        continue

    page_slug = None
    for m in game.get("catalogNs", {}).get("mappings", []):
        if m.get("pageType") == "productHome":
            page_slug = m.get("pageSlug")
            break

    if page_slug:
        free_games.append({
            "title": game["title"],
            "description": game["description"],
            "slug": page_slug
        })

# 📋 Mostrar menú
print("\n🎮 Juegos gratis disponibles:\n")
for i, game in enumerate(free_games, start=1):
    print(f"\033[92m[{i}]\033[0m \033[96m{game['title']}\033[0m\n     \033[93m{game['description']}\033[0m\n")

# 🔘 Botón por input
while True:
    choice = input("\nSelecciona un juego para DESCARGAR (0 para salir): ")

    if choice == "0":
        print("👋 Saliendo...")
        break

    if not choice.isdigit() or not (1 <= int(choice) <= len(free_games)):
        print("❌ Opción inválida")
        continue

    game = free_games[int(choice) - 1]
    print(f"🚀 Abriendo Epic Launcher para: {game['title']}")

    webbrowser.open(f"com.epicgames.launcher://store/p/{game['slug']}")
