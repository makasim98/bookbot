def get_num_words(text: str):
    return len(text.split())

def get_character_analysis(text: str):
    result: dict[str, int] = {}
    for c in text:
        if c.lower() not in result:
            result[c.lower()] = 0
        result[c.lower()] += 1
    
    return result

def sort_stats(stats: dict):
    return sorted(stats.items(), key=lambda x: x[1], reverse=True)
