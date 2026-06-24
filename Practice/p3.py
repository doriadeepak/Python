def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"

print(greet("en"),"Glen")
print(greet("es"), "Sally")
print(greet("fr"), "Aakhri pasta on London Rasta")