import yt_dlp

def search_youtube(text: str):
    ydl_opts = {
        'quiet': True,
        'default_search': 'ytsearch',
        'max_downloads': 1,
        'cookiefile': 'cookies.txt'  # Usa cookies.txt
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(text, download=False)
        if "entries" in info and info["entries"]:
            return info["entries"][0]["webpage_url"]  # URL correcta del video
    return "No se encontraron resultados"






