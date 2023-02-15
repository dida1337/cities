banned_words = ("'", ",", "!", "?", ":", ";", "%", "№", "-", "+", "=", "`", "~", "/", ".", ",", '"', "|", "<", ">")
async def check_name(name: str):
    if len(name) > 14:
        return False
    elif len(name) < 3:
        return False
    elif any(i in name for i in banned_words):
        return False
    else:
        return True


