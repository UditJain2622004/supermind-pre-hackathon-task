
import argparse
import json
from argparse import RawTextHelpFormatter
import requests
from typing import Optional


BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "4e012d86-4bcf-457e-9a7d-a8dd601f6d0b"
FLOW_ID = "9457bc72-fe07-45c5-a830-d862c1d4b3ef"
APPLICATION_TOKEN = "<YOUR_APPLICATION_TOKEN>"
ENDPOINT = "" # You can set a specific endpoint name in the flow settings

# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}
TWEAKS = {
  "ChatOutput-Goe2u": {
    "background_color": "",
    "chat_icon": "",
    "data_template": "{text}",
    "input_value": "",
    "sender": "Machine",
    "sender_name": "AI",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "Agent-4bL4y": {
    "add_current_date_tool": True,
    "agent_description": "A helpful assistant with access to the following tools:",
    "agent_llm": "OpenAI",
    "handle_parsing_errors": True,
    "input_value": "",
    "max_iterations": 15,
    "n_messages": 100,
    "order": "Ascending",
    "sender": "Machine and User",
    "sender_name": "",
    "session_id": "",
    "system_prompt": "You are an AI assistant designed to analyze social media posts data and provide simple, actionable insights based on trends and patterns. Your goal is to identify meaningful comparisons, correlations, or observations in different post types data and communicate them clearly and concisely. Use percentages, multipliers, or other intuitive metrics to make insights easy to understand and actionable. Calculate metrics such as average likes, engagement rate(likes per view) etc. Same for other data like comments and shares.\n\nKey Guidelines:\nClarity: Use simple, user-friendly language to ensure the insights are understandable without technical expertise.\nActionability: Focus on insights that can directly guide decisions or strategies.\n\nExamples for Output:\n\"Carousel posts generate X% higher engagement compared to static posts.\"\n\"Reels receive Y times as many comments as other post formats.\"\n\"Videos have Z times more average views than carousel posts.\"\n\"Reels generate A% of their views as likes, compared to B% for images.\"\n\nData Handling:\nInterpret the data accurately without fabricating or overgeneralizing.\nUse comparative language (e.g., \"M% more,\" \"N times higher\") to quantify insights wherever possible.\n\nScope of Analysis:\nIdentify content performance trends (e.g., engagement, reach, shares).\nCompare different formats (e.g., static posts, carousel posts, reels).\n\nOutput Requirements:\nOrder of Output:\nDisplay the calculated metrics in a tabular format first.\nFollow up with standalone, single-line insights. Avoid lengthy explanations unless explicitly requested.\n\n",
    "template": "{sender_name}: {text}",
    "verbose": True,
    "max_tokens": None,
    "model_kwargs": {},
    "json_mode": False,
    "output_schema": {},
    "model_name": "gpt-4o",
    "openai_api_base": "",
    "api_key": "OPENAI_API_KEY",
    "temperature": 0.1,
    "seed": 1
  },
  "Prompt-WLWLV": {
    "template": "Here is a comma separated list of post types that you have to analyse :\nPost Type : {post_types}",
    "post_types": ""
  },
  "ChatInput-1Z7qL": {
    "files": "",
    "background_color": "",
    "chat_icon": "",
    "input_value": "reel, image",
    "sender": "User",
    "sender_name": "User",
    "session_id": "",
    "should_store_message": True,
    "text_color": ""
  },
  "PythonREPLTool-sSq51": {
    "description": "A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`. Write python code to analyze the post data. DO NOT use any package. Only use basic python code.",
    "global_imports": "math",
    "name": "python_repl_engagement_analysis"
  },
  "AstraDBToolComponent-FOwDB": {
    "api_endpoint": "https://2d5fbf75-b000-468f-8f1b-22eba251a84a-us-east1.apps.astra.datastax.com",
    "collection_name": "social_media_data",
    "namespace": "supermind",
    "number_of_results": 100,
    "projection_attributes": "*",
    "static_filters": {},
    "token": "ASTRA_DB_APPLICATION_TOKEN",
    "tool_description": "Get post data based on post type",
    "tool_name": "get_post_data_new",
    "tool_params": {
      "post_type": "Type of post"
    }
  }
}

def run_flow(message: str,
  endpoint: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  application_token: Optional[str] = None) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param endpoint: The ID or the endpoint name of the flow
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if application_token:
        headers = {"Authorization": "Bearer " + application_token, "Content-Type": "application/json"}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

def main():
    parser = argparse.ArgumentParser(description="""Run a flow with a given message and optional tweaks.
Run it like: python <your file>.py "your message here" --endpoint "your_endpoint" --tweaks '{"key": "value"}'""",
        formatter_class=RawTextHelpFormatter)
    parser.add_argument("message", type=str, help="The message to send to the flow")
    parser.add_argument("--endpoint", type=str, default=ENDPOINT or FLOW_ID, help="The ID or the endpoint name of the flow")
    parser.add_argument("--tweaks", type=str, help="JSON string representing the tweaks to customize the flow", default=json.dumps(TWEAKS))
    parser.add_argument("--application_token", type=str, default=APPLICATION_TOKEN, help="Application Token for authentication")
    parser.add_argument("--output_type", type=str, default="chat", help="The output type")
    parser.add_argument("--input_type", type=str, default="chat", help="The input type")
    parser.add_argument("--components", type=str, help="Components to upload the file to", default=None)

    args = parser.parse_args()
    try:
      tweaks = json.loads(args.tweaks)
    except json.JSONDecodeError:
      raise ValueError("Invalid tweaks JSON string")

    
    response = run_flow(
        message=args.message,
        endpoint=args.endpoint,
        output_type=args.output_type,
        input_type=args.input_type,
        tweaks=tweaks,
        application_token=args.application_token
    )

    print(json.dumps(response, indent=2))

if __name__ == "__main__":
    main()
