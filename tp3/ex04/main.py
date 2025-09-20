url = "https://sistema.exemplo.com/busca?termo=velho"

updated_url = url.replace("velho", "novo")

def extract_term_parameter(url):
    start = url.find("termo=")
    if start == -1:
        return None
    start += len("termo=")
    end = url.find("&", start)
    if end == -1:
        end = len(url)
    return url[start:end]

print(updated_url)
print(extract_term_parameter(updated_url))
