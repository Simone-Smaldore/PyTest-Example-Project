import pytest
import math
import source.shapes as shapes


class TestCircle:

    def setup_method(self, method):
        """Function to setting up a method

        Args:
            method (function): The setting up method

        To print in the console call pytest -s
        """
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        """Function to tearing down a method

        Args:
            method (function): The tearing down method

        To print in the console call pytest -s
        """
        print(f"Tearing down {method}")
        del self.circle

    def test_area(self):
        result = self.circle.area()
        assert result == math.pi * (self.circle.radius**2)

    def test_perimeter(self):
        result = self.circle.perimeter()
        assert result == 2 * math.pi * self.circle.radius
