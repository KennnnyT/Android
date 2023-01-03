import re

def is_alphanumeric(string):
  # Utilise l'expression régulière pour vérifier si la chaîne de caractères est alphanumérique
  return bool(re.match(r'^[a-zA-Z0-9]+$', string))

# Test de la fonction
print(is_alphanumeric("abc123"))  # True
print(is_alphanumeric("abc123!"))  # False
print(is_alphanumeric("123"))     # True
print(is_alphanumeric("abc"))     # True
