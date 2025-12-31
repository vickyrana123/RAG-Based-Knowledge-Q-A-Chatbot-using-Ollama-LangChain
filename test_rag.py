import pytest
from rag import chatbot_ask
from cache import cache

def test_chatbot_response_exists():
    response = chatbot_ask("What is the main topic?")
    assert response is not None
    assert len(response) > 10, "Response is too short to be meaningful"

def test_retrieval_accuracy():
    query = "What is the specific definition of Problem 1?"
    response = chatbot_ask(query)
    
    assert "classification" in response.lower() or "expert" in response.lower()

def test_cache_functionality():
    question = "Explain RAG in one sentence."
    
    first_start = time.time()
    ans1 = chatbot_ask(question)
    first_duration = time.time() - first_start
    
    second_start = time.time()
    ans2 = chatbot_ask(question)
    second_duration = time.time() - second_start
    
    assert ans1 == ans2
    assert second_duration < first_duration, "Cache should be faster than LLM generation"

def test_empty_query():
    with pytest.raises(Exception): 
        chatbot_ask("")