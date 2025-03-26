from dotenv import load_dotenv
from openai import OpenAI
from mem0 import Memory

load_dotenv()

config = {
    "llm":{
        "provider": "openai",
        "config":{
            "model": "gpt-4o-mini",
        }
    }
}

openai_client = OpenAI()
memory = Memory.from_config(config)

def chat_with_memories(message: str, user_id: str= "default_user") -> str:
    relevant_memories = memory.search(query=message, user_id=user_id, limit=3)
    memories_str = "\n".join(f"-{entry['memory']}" for entry in relevant_memories["results"]) 

    system_prompt = f"You are a helpful assistant that can remember and recall information. Here are some memories that might be relevant to the conversation.\nUser Memories: \n{memories_str}"
    messages = [{"role": "system", "context": system_prompt}, {"role": "user", "content": message}]
    response = openai_client.chat.completions.create(model="gpt-4o-mini", messages=messages)
    assistant_response = response.choices[0].message.content()

    message.append({"role": "assistant", "content": assistant_response})
    memory.add(message, user_id=user_id)
    return assistant_response

def main():
    print("Welcome to the Mem0 Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        print(f"Assistant: {chat_with_memories(user_input)}")

if __name__ == "__main__":
    main()

