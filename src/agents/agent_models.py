from autogen_ext.models.openai import OpenAIChatCompletionClient
from src.schema.response_schema import PriorityListResponse, SpecialistResponse, ChatResponse

gp_model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    response_format=PriorityListResponse
)

specialist_model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    response_format=SpecialistResponse
)

chat_model_client = OpenAIChatCompletionClient(
    model="gpt-4o",
    response_format=ChatResponse
)
