import google.generativeai as genai

genai.configure(api_key='')

#listar os modelos da Gemini disponíveis
'''
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
'''

#print(response.text)


def get_instrument_ai_bio(product, model):
    model_ai = genai.GenerativeModel('gemini-pro')
    if model:
        prompt = f"Me mostre uma descrição de venda para o produto {product} {model} em apenas 250 caracteres. Fale coisas específicas desse produto"
    elif product:
        prompt = f"Me mostre uma descrição de venda para o produto {product} em apenas 250 caracteres. Fale coisas específicas desse produto"
    else:
        prompt = f"Diga que o usuário não cadastrou o nome e/ou o modelo do produto"

    response = model_ai.generate_content(prompt)

    bio = response.candidates[0].content.parts[0].text
    return bio
