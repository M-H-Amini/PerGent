from openai import AsyncOpenAI
import asyncio


async def generate_persona(task: str):
    client = AsyncOpenAI(
        api_key=open("api.txt").read().strip()
    )

    system_message = open("oneshot_generator.txt").read().strip()

    response = await client.responses.create(
        model="gpt-4o",
        input=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": task},
        ],
    )

    return response.output_text


async def main():
    task = "Generate a persona for a supply planner."

    persona = await generate_persona(task)

    print("-" * 20)
    print(persona)


if __name__ == "__main__":
    asyncio.run(main())