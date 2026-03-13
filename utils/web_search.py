from duckduckgo_search import DDGS

def search_web(query):

    results = []

    try:
        with DDGS() as ddgs:
            for r in ddgs.text(query, max_results=3):
                results.append(r["body"])
    except:
        results.append("No web results")

    return "\n".join(results)
