def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    rho = 998.2  # density of water in kg/m^3
    pressure_loss = (-0.04 * rho * fluid_velocity**2 * quantity_fittings) / 2000
    return pressure_loss

def reynolds_number(hydraulic_diameter, fluid_velocity):
    rho = 998.2  # density of water in kg/m^3
    mu = 0.0010016  # dynamic viscosity in Pa·s
    reynolds = (rho * hydraulic_diameter * fluid_velocity) / mu
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    rho = 998.2  # density of water in kg/m^3
    k = 0.1 + (50 / reynolds_number) * ((larger_diameter / smaller_diameter)**4 - 1)
    pressure_loss = (-k * rho * fluid_velocity**2) / 2000
    return pressure_loss

def water_column_height(tower_height, tank_height):
    """Calculate the height of the water column above the house."""
    return tower_height + (tank_height / 2)

def pressure_gain_from_water_height(height):
    """Calculate the pressure gain from a column of water of a given height."""
    rho = 998.2  # density of water in kg/m^3
    g = 9.80665  # acceleration due to gravity in m/s^2
    return rho * g * height / 1000  # convert to kilopascals

def pressure_loss_from_pipe(diameter, length, friction_factor, velocity):
    """Calculate the pressure loss from pipe friction."""
    rho = 998.2  # density of water in kg/m^3
    pressure_loss = (-friction_factor * length * rho * velocity**2) / (2 * diameter * 1000)
    return pressure_loss

# Constants (provided in the assignment)
PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013   # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018    # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()

    from pytest import approx
import pytest
from water_flow import (water_column_height, pressure_gain_from_water_height,
                        pressure_loss_from_pipe, pressure_loss_from_fittings,
                        reynolds_number, pressure_loss_from_pipe_reduction)

def test_pressure_loss_from_fittings():
    # Test cases from the assignment
    assert pressure_loss_from_fittings(0.00, 3) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == approx(-0.306, abs=0.001)

def test_reynolds_number():
    # Test cases from the assignment
    assert reynolds_number(0.048692, 0.00) == approx(0, abs=1)
    assert reynolds_number(0.048692, 1.65) == approx(80069, abs=1)
    assert reynolds_number(0.048692, 1.75) == approx(84922, abs=1)
    assert reynolds_number(0.286870, 1.65) == approx(471729, abs=1)
    assert reynolds_number(0.286870, 1.75) == approx(500318, abs=1)

def test_pressure_loss_from_pipe_reduction():
    # Test cases from the assignment
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

# Additional test cases for exceeding requirements
def test_pressure_loss_from_fittings_edge_cases():
    # Test with very high velocity
    assert pressure_loss_from_fittings(100.0, 1) == approx(-1996.4, abs=0.1)
    # Test with negative velocity (should be same as positive due to v^2)
    assert pressure_loss_from_fittings(-1.65, 2) == approx(-0.109, abs=0.001)

def test_reynolds_number_edge_cases():
    # Test with very small diameter
    assert reynolds_number(0.0001, 1.65) == approx(164.5, abs=1)
    # Test with very high velocity
    assert reynolds_number(0.048692, 100.0) == approx(4.853e6, abs=1e3)

def test_pressure_loss_from_pipe_reduction_edge_cases():
    # Test with very small diameter ratio
    assert pressure_loss_from_pipe_reduction(0.1, 1.65, 100000, 0.099) == approx(-0.273, abs=0.001)
    # Test with very large Reynolds number
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 1e9, 0.048692) == approx(-1.361, abs=0.001)