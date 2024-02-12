import pytest
import source.shapes as shapes


@pytest.fixture
def my_rectangle() -> shapes.Rectangle:
    return shapes.Rectangle(10, 5)


def test_area_rectangle(my_rectangle: shapes.Rectangle):
    assert my_rectangle.area() == 50


def test_perimeter_rectangle(my_rectangle: shapes.Rectangle):
    assert my_rectangle.perimeter() == 30


def test_equals_rectangle(
    my_rectangle: shapes.Rectangle, other_rectangle: shapes.Rectangle
):
    assert not my_rectangle == other_rectangle
