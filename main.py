import openai
from key import s_key

openai.api_key = s_key

def chat_with_gpt(prompt):
    response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.7,
  )
    return response.choices[0].text.strip()

def create_html_file(filename, response):
    with open(filename, 'w') as file:
        file.write(response)

with open('article.txt', 'r') as article:
    text = article.read()


my_prompt = 'Jesteś programistą, inzynierem promptów oraz blogerem. Przeanalizuj cały ponizszy tekst pod kątem poprawności językowej oraz stylistycznej. Tekst powinien przypominać artykuł. Następnie przekształć go na kod HTML, wszystkie elementy powinny być zawarte w poprawnych tagach, wewnątrz tagu <body>. Zaproponuj kilka miejsc, w których mogłyby pojawić się zdjęcia, kazde takie miejsce oznacz tagiem <img> z atrybutami src, którego wartości zawsze wynosi:"image_placeholder.jpg" oraz atrybut alt="[opis obrazu]", gdzie [opis obrazu] powinien być precyzyjnym opisem (składającym się z trzech zdań) potencjalnego obrazu ilustrującego treść poprzedniego akapitu. Opis ten powinien być sformułowany w taki sposób, aby można go było wykorzystać jako idealny prompt do wygenerowania odpowiedniego obrazu. Pod obrazkiem dodaj równiez tag <figcaption> zawierający krótką wersje [opis obrazu], całość zawrzyj w tagu <figure> ' + text


response = chat_with_gpt(my_prompt)

create_html_file("artykul.html",response)

print(response)

