##
# Author: Marcos Antonio de Carvalho
# eMAil.: marcos.antonio.carvalho@gmail.com
# GitHub: https://github.com/owl-arch
# Descr.: Criar uma classe Python personalizada para converter
#         dados JSON para objeto Python personalizado.
##
# Inspiração: https://medium.com/@siddharthgov01/regular-expressions-from-a-za-z-88cf9cf0abac

import re # RegEx Python

##
# Meta Characters: -
##

# Sequências Especiais
text = "x8989072"  
x = r'\A[a-zA-Z][0-9]+'

result = bool(re.match(x, text))
print(result)  # Output: True

# A função search() em Regex
text = "Stop Scrolling Instagram, Start Learning Python"
x = re.search(r"S", text)
print(x)
# Output: <re.Match object; span=(0, 1), match='S'>

# A função findall() em Regex
text = "AI's AI coded AI for AI to decipher AI's complex AI algorithms."
x = re.findall(r"AI", text)
print(x)
# Output: ['AI', 'AI', 'AI', 'AI', 'AI', 'AI']

# A função sub() em Regex
text = "Anxious alligators awkwardly assembled, eagerly awaiting their afternoon appetizer."
x = re.sub("a", "@", text)
print(x)
# Output: Anxious @llig@tors @wkw@rdly @ssembled, e@gerly @w@iting their @fternoon @ppetizer.

# A função split() em Regex
txt = "AI wrote a poem; roses are #FF0000, violets are #0000FF."
x = re.split("\s", txt)
print(x)
# Output: ['AI', 'wrote', 'a', 'poem;', 'roses', 'are', '#FF0000,', 'violets', 'are', '#0000FF.']

# Classes de caracteres
text = "Python has different libraries such as pandas, numpy, pytorch, scikit-learn, etc"
x = re.findall(r"[^aeiou\s]", text)
print(x)

# Quantificadores
text = "My email address is regexxy8008@python.com and my phone number is 45"
x = re.findall(r"[0-9]{3,4}", text)
print(x)
# Output: ['8008']

# Olhe para frente (Lookaheads)
text = "I love pineapple juice, but I do not like pineapple ice-cream."
result = re.findall(r'pineapple(?= juice)', text)

if result:
    print("Found 'pineapple' followed by 'juice'")
    print(result)  
else:
    print("No match found")

# Olhe atrás (Lookbehinds)
text = "A red flower is my favourite, but blue flower is my father's favourite."
result = re.findall(r'(?<!blue )flower', text)

if result:
    print("Found 'flower' not preceded by 'blue'")
    print(result)
else:
    print("No match found") 

##
# Aqui estão algumas maneiras complexas de usar Regex:
##

# Validação de e-mail      
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))  

print(validate_email("user@example.com"))  # True
print(validate_email("invalid. Email"))    # False

# Removedor de tags HTML
def remove_html_tags(text):
    pattern = r'<.*?>'
    return re.sub(pattern, '', text)

html_text = "<p>This is <b>bold</b> text.</p>"
print(remove_html_tags(html_text)) 
# Output: "This is bold text."

# Extraindo dados de determinado texto
def extract_dates(text):
    pattern = r'\d{2}/\d{2}/\d{4}'
    return re.findall(pattern, text)

unstructured_text = "Meeting on 12/25/2023 and 01/15/2024"
print(extract_dates(unstructured_text)) 
# Output: ['12/25/2023', '01/15/2024']

# Verificador de força da senha
def check_password_strength(password):
    if re.match(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&\_])[A-Za-z\d@#$%&\_]{8,}$', password):
        return "Strong"
    else:
        return "Weak"

print(check_password_strength("P@ssw0rd"))  # Strong
print(check_password_strength("password"))  # Weak

# Validação de endereço IP
def validate_ip(ip):
    pattern = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return all(re.match(pattern, part) for part in ip.split('.'))

print(validate_ip("192.168.1.1"))     # True
print(validate_ip("256.256.256.256")) # False

# Tokenização
text = "He didn't want to go, but he had to. She said, 'It's time.'"
tokens = re.findall(r"\b\w+(?:[-']\w+)*\b|[.,!?';]", text)
print(tokens)
