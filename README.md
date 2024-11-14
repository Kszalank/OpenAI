# OpenAI
Aplikacja łączy się z API OpenAI przy użyciu klucza. Następnie otwiera plik tekstowy article.txt i zapisuje jego zawartość w zmiennej **text**. Następnie prompt wraz z zmienną **text** przekazywany jest jako prompt do OpenAI przy użyciu funkcji **chat_with_gpt()**.
Odpowiedź otrzymana w postaci zmiennej **response** od ChatuGPT zapisana jest w postaci pliku HTML za pomocą funkcji **create_html_file()** zgodnie z wytycznymi zadania.

Aplikacja została napisana przy użyciu VS Code, aplikację należy uruchomić w otwartym pliku main.py przy użyciu przycisku "Run Python File".
