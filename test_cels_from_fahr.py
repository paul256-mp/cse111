from weather import cels_from_fahr
from pytest import approx
import pytest
def test_cels_from_fahr():
  """Test cases for cels_from_fahr function."""
  # test for the range of fah  assert cels_from_fahr(-40)== approx(-60
  assert cels_from_fahr(-32)== approx(-35.55555555555556)
  assert cels_from_fahr(0)== approx(-17.77777777777778)
  assert cels_from_fahr(32)== approx(0)
  assert cels_from_fahr(100)== approx(37.77777777777778)
]pytest.main()