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