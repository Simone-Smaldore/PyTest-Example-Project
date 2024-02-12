import pytest
import source.shapes as shapes


@pytest.mark.parametrize("side, area", [(4, 16), (5, 25), (6, 36), (2, 4)])
def test_multiple_side_area(side, area):
    assert shapes.Square(side).area() == area


@pytest.mark.parametrize("side, perimeter", [(4, 16), (5, 20), (6, 24), (2, 8)])
def test_multiple_side_perimeter(side, perimeter):
    assert shapes.Square(side).perimeter() == perimeter
