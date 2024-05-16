import openai

# Configura tu clave de API de OpenAI
openai.api_key = ''

# Función para obtener una respuesta de ChatGPT
def get_chatgpt_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    # Corregido: Asegúrate de devolver la parte correcta de la respuesta
    return response['choices'][0]['message']['content']

# Ejemplo de uso de la función
prompt = "Hola, ¿cómo estás?"
# Corregido: Asegúrate de imprimir la respuesta de la función
print(get_chatgpt_response(prompt))
