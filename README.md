# Mem0 Agent - Memory-Powered AI Assistant

This project implements an AI assistant with memory capabilities using Mem0, OpenAI, and Supabase. The agent can remember past conversations and use them to provide context-aware responses.

## Current Implementation

### Core Components
1. **Memory Management (Mem0)**
   - Stores and retrieves conversation history
   - Uses vector embeddings for semantic search
   - Maintains user-specific memories

2. **Language Model (OpenAI)**
   - Uses GPT-3.5-turbo for response generation
   - Incorporates memory context in prompts
   - Provides natural language responses

3. **Database (Supabase)**
   - Stores vector embeddings
   - Handles user authentication
   - Manages conversation history

### Setup Requirements
1. Environment Variables:
```env
OPENAI_API_KEY=your_openai_key
MEM0_API_KEY=your_mem0_key
DATABASE_URL=your_supabase_connection_string
```

2. Dependencies:
```bash
pip install python-dotenv openai mem0ai vecs psycopg2-binary
```

## Future Expansion Options

### 1. UI Options

#### A. Streamlit Interface
```python
import streamlit as st

def streamlit_ui():
    st.title("Mem0 Chat Interface")
    user_input = st.text_input("Your message:")
    if st.button("Send"):
        response = chat_with_memories(user_input)
        st.write(f"Assistant: {response}")
```

#### B. FastAPI Backend + React Frontend
- FastAPI for RESTful endpoints
- React for modern, responsive UI
- WebSocket support for real-time chat

#### C. Gradio Interface
```python
import gradio as gr

def gradio_interface():
    iface = gr.Interface(
        fn=chat_with_memories,
        inputs=gr.Textbox(lines=2),
        outputs=gr.Textbox(lines=5),
        title="Mem0 Chat"
    )
    iface.launch()
```

### 2. Supabase Integration Options

#### A. User Authentication
```python
from supabase import create_client

supabase = create_client(
    supabase_url=os.getenv("SUPABASE_URL"),
    supabase_key=os.getenv("SUPABASE_KEY")
)
```

#### B. Vector Store Configuration
```python
config = {
    "vector_store": {
        "provider": "supabase",
        "config": {
            "connection_string": database_url,
            "collection_name": "memories",
            "embedding_model_dims": 1536,
            "index_measure": "cosine_distance",
            "index_method": "ivfflat"
        }
    }
}
```

### 3. Additional Features

1. **Memory Management**
   - Memory summarization
   - Memory deletion/editing
   - Memory categories/tags

2. **User Experience**
   - Conversation history view
   - Memory visualization
   - Export/import memories

3. **Advanced Features**
   - Multi-user support
   - Memory sharing
   - Custom memory types

## Getting Started

1. Clone the repository
2. Set up environment variables
3. Install dependencies
4. Run the agent:
```bash
python v1-mem0.py
```

## Contributing

Feel free to contribute by:
1. Adding new features
2. Improving documentation
3. Fixing bugs
4. Suggesting improvements

## License

MIT License - feel free to use this project for your own purposes. 