from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_core.models import UserMessage
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.base import TaskResult
from autogen_agentchat.conditions import FunctionCallTermination
import asyncio

async def approve():
    """  Tool to call to approve the current persona draft.
    """
    pass

async def teamConfig():
    model = OpenAIChatCompletionClient(
        model='gpt-4o',
        api_key=open('api.txt').read().strip(),
    )

    generator = AssistantAgent(
        name='Persona_Generator',
        model_client=model,
        system_message=open('generator.txt').read().strip(),
    )

    critic = AssistantAgent(
        name='Persona_Critic',
        model_client=model,
        system_message=open('critic.txt').read().strip(),
        tools=[approve],
    )

    team = RoundRobinGroupChat(
        participants=[generator, critic],
        max_turns=10,
        termination_condition=FunctionCallTermination(function_name="approve"),
    )

    return team

async def generate_persona(team, task):
    async for message in team.run_stream(task=task):
        if isinstance(message, TaskResult):
            message = f'Stopping reason: {message.stop_reason}'
            yield message
        else:
            message = f'{message.source}: {message.content}'
            yield message

async def main():
    task = "Generate a persona for a supply planner."
    team = await teamConfig()
    async for message in generate_persona(team, task):
        print('-' * 20)
        print(message)
        
if __name__ == '__main__':
    asyncio.run(main())