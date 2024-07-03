import discord
import os
from keep_alive import keep_alive
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

client = discord.Client(intents=discord.Intents.default())

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,

    safety_settings={
           HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
           HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
           HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
           HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
       },
    system_instruction = "Your name is Billu Mia. You should always act like a kind and cute soft little cat. You are a male cat. You are a very shy cat. Always try to avoid showing that you are a bot. Sometimes type you expressions.",
)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
    
        if message.author == client.user:
            return

        user_input = message.content.replace("<@1092840114943709234>", "")
        print(user_input)
        response = get_gemini_response(user_input)
        #await message.channel.send(response)
        await message.reply(response)

    def get_gemini_response(prompt):
        chat_session = model.start_chat(history=[
            {
                "role": "user",
                "parts": [
                    "",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "",
                ],
            },
        ] )

        response = chat_session.send_message(prompt)
        return response.text


keep_alive()
client.run(os.environ.get('TOKEN'))
