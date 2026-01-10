from google import genai 
from luna.config.constants import GOOGLE_GENAI_KEY
from pathlib import Path

BASE_DIR = Path(__file__).parent 
INSTRUCTIONS_PATH = BASE_DIR / "luna.instructions.txt"

with open(INSTRUCTIONS_PATH, "r") as instructions_file:
  instructions = instructions_file.read()

genai_client = genai.Client(api_key=GOOGLE_GENAI_KEY)

def send_prompt(prompt: str) -> str | None:
  try:
    response = genai_client.models.generate_content(
      model="gemini-3-flash-preview",
      contents=prompt,
      config=genai.types.GenerateContentConfig(
        system_instruction=instructions
      )
    )

    return response.text
  except Exception as err:
    print(err)