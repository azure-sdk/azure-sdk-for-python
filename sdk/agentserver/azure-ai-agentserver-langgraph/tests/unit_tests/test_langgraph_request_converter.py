"""
Unit tests for the LangGraph invoke handler message conversion.

Tests ``_to_langchain_messages`` from ``azure.ai.agentserver.langgraph.invoke``.
"""

import pytest
from langchain_core import messages as lc_messages

from azure.ai.agentserver.langgraph.invoke import _to_langchain_messages


@pytest.mark.unit
def test_convert_implicit_user_message():
    """Implicit user message (dict with 'content' key) → HumanMessage."""
    input_data = [{"content": "input text string"}]
    result = _to_langchain_messages(input_data)

    assert len(result) == 1
    assert isinstance(result[0], lc_messages.HumanMessage)
    assert result[0].content == "input text string"


@pytest.mark.unit
def test_convert_plain_string():
    """Plain string input → HumanMessage."""
    result = _to_langchain_messages(["hello world"])

    assert len(result) == 1
    assert isinstance(result[0], lc_messages.HumanMessage)
    assert result[0].content == "hello world"


@pytest.mark.unit
def test_convert_content_list_with_input_text():
    """Content list with input_text items → joined text in HumanMessage."""
    input_data = [{"content": [{"type": "input_text", "text": "Hello"}, {"type": "input_text", "text": "world"}]}]
    result = _to_langchain_messages(input_data)

    assert len(result) == 1
    assert isinstance(result[0], lc_messages.HumanMessage)
    assert result[0].content == "Hello world"


@pytest.mark.unit
def test_convert_role_based_messages():
    """Explicit role-based messages → correct LangChain message types."""
    input_data = [
        {"role": "user", "content": "user message"},
        {"role": "assistant", "content": "assistant message"},
        {"role": "system", "content": "system message"},
    ]
    result = _to_langchain_messages(input_data)

    assert len(result) == 3
    assert isinstance(result[0], lc_messages.HumanMessage)
    assert isinstance(result[1], lc_messages.AIMessage)
    assert isinstance(result[2], lc_messages.SystemMessage)
    assert result[0].content == "user message"
    assert result[1].content == "assistant message"
    assert result[2].content == "system message"


@pytest.mark.unit
def test_convert_text_type_item():
    """Item with type=text → HumanMessage with text content."""
    input_data = [{"type": "text", "text": "typed text item"}]
    result = _to_langchain_messages(input_data)

    assert len(result) == 1
    assert isinstance(result[0], lc_messages.HumanMessage)
    assert result[0].content == "typed text item"


@pytest.mark.unit
def test_convert_empty_list():
    """Empty input list → empty result."""
    result = _to_langchain_messages([])
    assert result == []


@pytest.mark.unit
def test_convert_unknown_role_defaults_to_human():
    """Unknown role → defaults to HumanMessage."""
    input_data = [{"role": "custom_role", "content": "some text"}]
    result = _to_langchain_messages(input_data)

    assert len(result) == 1
    assert isinstance(result[0], lc_messages.HumanMessage)
    assert result[0].content == "some text"
