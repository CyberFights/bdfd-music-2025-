from youtube_search import YoutubeSearch
import json

def search_youtube(text: str):
    results = YoutubeSearch(text, max_results=1).to_json()
    data = json.loads(results)  # Convertir la cadena JSON en un diccionario
    if data["videos"]:
        video_id = data["videos"][0]["id"]
        return f"https://www.youtube.com/watch?v={video_id}"
    return "No se encontraron resultados"

