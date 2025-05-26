from pytest import approx
import pytest
from water_flows import (water_column_height, pressure_gain_from_water_height, 
                         pressure_loss_from_pipe, pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction)

def test_water_column_height():
    """Test cases for water_column_height function"""
    # Test when both tower and tank heights are 0
    assert water_column_height(0, 0) == approx(0)
    # Test when tower height is 0 but tank height is 10
    assert water_column_height(0, 10) == approx(7.5)
    # Test when tank height is 0 but tower height is 25
    assert water_column_height(25, 0) == approx(25.0)
    # Test with non-zero tower and tank heights
    assert water_column_height(48.3, 12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    """Test cases for pressure_gain_from_water_height function"""
    # Test with zero height
    assert pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)
    # Test with a moderate height
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    # Test with a larger height
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    """Test cases for pressure_loss_from_pipe function"""
    # Test with zero pipe length (should be zero loss)
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)
    # Test with zero friction factor (should be zero loss)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs=0.001)
    # Test with zero fluid velocity (should be zero loss)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs=0.001)
    # Normal case with all non-zero parameters
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    # Same as above but with slightly lower velocity
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    # Larger diameter and longer pipe
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)
    # Similar to above but with longer pipe length
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

  
def test_pressure_loss_from_fittings():
  assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, abs=0.001)
  assert pressure_loss_from_fittings(1.65, 0) == approx(0.000	, abs=0.001)
  assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
  assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
  assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)


def test_reynolds_number():
  assert reynolds_number(0.048692, 0.00) == approx(0, abs=1)
  assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
  assert reynolds_number(0.048692, 1.75, ) == approx(84922, abs=1)
  assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)
  assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
  assert pressure_loss_from_pipe_reduction(0.28687	, 0.00, 1,0.048692	)  == approx(0.000, abs=0.001)
  assert pressure_loss_from_pipe_reduction(0.28687, 1.65 ,471729 ,0.048692	) == approx(-163.744, abs=0.001)
  assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318 ,0.048692 ) == approx(-184.182, abs=0.001)



pytest.main(["-v", "--tb=line", "-rN", __file__])