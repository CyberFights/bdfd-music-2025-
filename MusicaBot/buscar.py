import yt_dlp

def search_youtube(text: str):
    ydl_opts = {
        'quiet': True,
        'default_search': 'ytsearch',
        'max_downloads': 1,
        'extract_flat': True,  # No descargar, solo obtener información
        'cookiefile': 'cookies.txt'  # Usa el archivo de cookies directamente
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(text, download=False)
        if "entries" in info and info["entries"]:
            return info["entries"][0]["url"]  # URL directa del video
    return "No se encontraron resultados"

print(search_youtube("zoe -azul"))


