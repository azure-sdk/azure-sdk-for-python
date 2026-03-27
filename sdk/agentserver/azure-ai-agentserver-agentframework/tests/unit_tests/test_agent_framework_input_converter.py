"""
Unit tests for the MAF invoke handler input/output conversion.

Tests ``_to_maf_input``, ``_extract_input_text``, ``_response_from_result``,
and ``_build_resume_input`` from ``azure.ai.agentserver.agentframework.invoke``.
"""

import pytest

from azure.ai.agentserver.agentframework.invoke import (
    _extract_input_text,
    _response_from_result,
    _to_maf_input,
)


# ------------------------------------------------------------------
# _extract_input_text tests
# ------------------------------------------------------------------

@pytest.mark.unit
def test_extract_text_from_plain_string():
    assert _extract_input_text("hello") == "hello"


@pytest.mark.unit
def test_extract_text_from_text_type():
    assert _extract_input_text({"type": "text", "text": "typed"}) == "typed"


@pytest.mark.unit
def test_extract_text_from_content_string():
    assert _extract_input_text({"content": "simple"}) == "simple"


@pytest.mark.unit
def test_extract_text_from_content_list():
    item = {"content": [{"text": "part1"}, {"text": "part2"}]}
    assert _extract_input_text(item) == "part1 part2"


# ------------------------------------------------------------------
# _to_maf_input tests (requires agent_framework)
# ------------------------------------------------------------------

@pytest.mark.unit
def test_to_maf_input_plain_string():
    """Plain string → single ChatMessage."""
    try:
        from agent_framework import ChatMessage

        result = _to_maf_input(["How are you?"])
        assert isinstance(result, ChatMessage)
        assert result.text == "How are you?"
    except ImportError:
        # Fallback path — returns joined string
        result = _to_maf_input(["How are you?"])
        assert result == "How are you?"


@pytest.mark.unit
def test_to_maf_input_multiple_messages():
    """Multiple items → list of ChatMessages."""
    try:
        from agent_framework import ChatMessage

        result = _to_maf_input(["first", "second"])
        assert isinstance(result, list)
        assert len(result) == 2
        assert all(isinstance(m, ChatMessage) for m in result)
    except ImportError:
        result = _to_maf_input(["first", "second"])
        assert result == "first second"


@pytest.mark.unit
def test_to_maf_input_empty_list():
    """Empty list → None."""
    result = _to_maf_input([])
    assert result is None or result == ""


@pytest.mark.unit
def test_to_maf_input_role_mapping():
    """Role-based items → correct ChatRole mapping."""
    try:
        from agent_framework import ChatMessage, Role as ChatRole

        result = _to_maf_input([{"role": "user", "content": "hello"}])
        assert isinstance(result, ChatMessage)
        assert result.role == ChatRole.USER
    except ImportError:
        result = _to_maf_input([{"role": "user", "content": "hello"}])
        assert result == "hello"


# ------------------------------------------------------------------
# _response_from_result tests
# ------------------------------------------------------------------

class _FakeTextContent:
    def __init__(self, text):
        self.text = text


class _FakeFunctionCallContent:
    def __init__(self, name, call_id, arguments=None):
        self.name = name
        self.call_id = call_id
        self.arguments = arguments or {}


class _FakeMessage:
    def __init__(self, contents):
        self.contents = contents


class _FakeResult:
    def __init__(self, messages):
        self.messages = messages


@pytest.mark.unit
def test_response_from_result_completed():
    """Normal text result → status=completed."""
    result = _FakeResult([_FakeMessage([_FakeTextContent("Hello!")])])
    response = _response_from_result(result)
    assert response["status"] == "completed"
    assert response["message"] == "Hello!"
    assert "interrupt" not in response


@pytest.mark.unit
def test_response_from_result_with_interrupt():
    """Function call content → status=requires_input + interrupt dict."""
    result = _FakeResult([
        _FakeMessage([_FakeFunctionCallContent("search", "call_1", {"q": "test"})])
    ])
    response = _response_from_result(result)
    assert response["status"] == "requires_input"
    assert response["interrupt"]["function_name"] == "search"
    assert response["interrupt"]["id"] == "call_1"


@pytest.mark.unit
def test_response_from_result_empty():
    """No messages → status=completed, message=None."""
    result = _FakeResult([])
    response = _response_from_result(result)
    assert response["status"] == "completed"
    assert response["message"] is None


@pytest.mark.unit
def test_response_from_result_preserves_first_interrupt():
    """Multiple interrupts → only first one is preserved."""
    result = _FakeResult([
        _FakeMessage([
            _FakeFunctionCallContent("first_fn", "call_1"),
            _FakeFunctionCallContent("second_fn", "call_2"),
        ])
    ])
    response = _response_from_result(result)
    assert response["interrupt"]["function_name"] == "first_fn"
