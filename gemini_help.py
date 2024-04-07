import google.generativeai as genai


genai.configure(api_key=)
model = genai.GenerativeModel('gemini-pro')




def gerar_resposta(info):
  model.generate_content(info)
