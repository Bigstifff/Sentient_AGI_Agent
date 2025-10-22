from sentient_agent_framework import AbstractAgent, DefaultServer, ResponseHandler
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

class DefiResearcher(AbstractAgent):
    async def assist(self, query, session, response_handler: ResponseHandler):
        prompt = f"You're a crypto research expert. Answer clearly\n{query}"

        header = {
            "Authorisation": f"bearer {os.getenv("SENTIENT_API_KEY")}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "accounts/sentientfoundation/model/dobby-unhinged-llama-3-3-70b-new",
            "messages": [{"role": "user", "content": prompt}],
            "max_token": 150
        }

        async with httpx.AsyncClient() as client:
            response = await client.post("https://api.fireworks.ai/inference/v1/chat/completions", 
                                         headers = header, 
                                         json = payload)
            response.raise_for_status()
            data = response.json() 
            await response_handler.emit_text(data['choices'][0]['message']['content'])

if __name__ == "__main__":
    agent = DefiResearcher("RoboX")
    server = DefaultServer(agent)
    try:
        print("Attempting to run server on port 8080...")
        server.run(port=8080)
    except Exception as e:
        print(f"Server failed to start due to an error: {e}")