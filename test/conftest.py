import pytest
import source.shapes as shapes


@pytest.fixture
def other_rectangle() -> shapes.Rectangle:
    return shapes.Rectangle(5, 5)
