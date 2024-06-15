from cmd import PROMPT
from urllib import response
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": PROMPT},
    {"role": "user", "content": PROMPT}
  ]
)

response(completion.choices[0].message);