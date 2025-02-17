def get_llm_response(question: str, context: str) -> str:
    """
    A mock function that simulates a local LLM's response.
    It takes in a question and some context (e.g., information about the image)
    and returns a canned response.
    """
    # For now, simply return a mock answer incorporating the inputs.
    return (
        f"Mock LLM Response: Based on the context '{context}', "
        f"the answer to your question '{question}' is 'This is a test answer.'"
    )