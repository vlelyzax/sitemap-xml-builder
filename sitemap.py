def build_sitemap(urls: list[str]) -> str:
    items = ''.join(f'<url><loc>{u}</loc><changefreq>weekly</changefreq></url>' for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{items}</urlset>'
