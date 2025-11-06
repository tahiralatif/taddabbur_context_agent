from agents import Agent, OpenAIChatCompletionsModel, AsyncOpenAI, Runner, RunConfig, ModelSettings
import os
from dotenv import load_dotenv
import asyncio
import pandas as pd

# Load .env
load_dotenv()
FIRE_WORKS_API = os.getenv("GEMINI_API_KEY")
if not FIRE_WORKS_API:
    raise ValueError("API_KEY not found in environment variables.")

# CSV path
CSV_PATH = "asbabul_nuzul_text.csv"

async def main():
    
    df = pd.read_csv(CSV_PATH)
    texts = df['text'].tolist()
    
    
    csv_content = "\n\n".join(texts[:50])  
    # Initialize LLM client
    client = AsyncOpenAI(
        api_key= FIRE_WORKS_API,
        base_url="https://api.fireworks.ai/inference/v1"
    )

    llm_model = OpenAIChatCompletionsModel(
        model="accounts/fireworks/models/gpt-oss-20b",
        openai_client=client
    )

    config = RunConfig(
        model=llm_model,
        model_provider=client,
        tracing_disabled=True
    )

    # Define agent
    agent = Agent(
        name="Tadabbur Context Agent",
        instructions=(
            "You are a Quranic Context Agent. Read this CSV content and suggest the necessary columns "
            "for structuring the Asbabul Nuzul data for AI embedding and retrieval. "
            "For each column, provide its name and purpose.\n\n"
            f"CSV content:\n{csv_content}"
        ),
        
    )

    # Run agent
    result = await Runner.run(
        starting_agent=agent,
        input="tell me the most important part of the history of the quran and also tell the sourceof which line and which number", 
        run_config=config
    )

    
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
