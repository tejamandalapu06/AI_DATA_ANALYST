from ai_insights import ask_ai

def data_chat(question, data):

    prompt = f"""
    You are an expert Data Analyst.

    Use the sales dataset below to answer the user's question.

    Dataset:

    {data}

    User Question:

    {question}
    """

    return ask_ai(prompt)