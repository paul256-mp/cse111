def water_column_height(tower_height, tank_height):
    """
    Calculate the height of a water column based on tower height and tank wall height.
    
    Args:
        tower_height (float): Height of the tower in meters.
        tank_height (float): Height of the tank walls on top of the tower in meters.
    
    Returns:
        float: Height of the water column in meters.
    """
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    """
    Calculate the pressure caused by Earth's gravity pulling on water in an elevated tank.
    
    Args:
        height (float): Height of the water column in meters.
    
    Returns:
        float: Pressure in kilopascals (kPa).
    """
    density = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    pressure = (density * gravity * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """
    Calculate water pressure lost due to friction between water and pipe walls.
    
    Args:
        pipe_diameter (float): Diameter of the pipe in meters.
        pipe_length (float): Length of the pipe in meters.
        friction_factor (float): Pipe's friction factor.
        fluid_velocity (float): Velocity of water in meters/second.
    
    Returns:
        float: Pressure loss in kilopascals (kPa).
    """
    density = 998.2  # kg/m^3
    numerator = -friction_factor * pipe_length * density * fluid_velocity**2
    denominator = 2000 * pipe_diameter
    pressure_loss = numerator / denominator
    return pressure_loss

from pytest import approx
import pytest
# Functions are defined above; no need to import from water_flow.

def test_water_column_height():
    assert water_column_height(0.0, 0.0) == approx(0.0)
    assert water_column_height(0.0, 10.0) == approx(7.5)
    assert water_column_height(25.0, 0.0) == approx(25.0)
    assert water_column_height(48.3, 12.8) == approx(57.9)

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == approx(0.0, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692, 0.00, 0.018, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.000, 1.75) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 0.00) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.75) == approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe(0.048692, 200.00, 0.018, 1.65) == approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1000.00, 0.013, 1.65) == approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe(0.286870, 1800.75, 0.013, 1.65) == approx(-110.884, abs=0.001)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])