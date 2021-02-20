import math

def gumball_approximation(jar_radius, jar_height, gumball_radius):
    '''
    Returns the number of gumballs that fit into a jar according to the above 
    dimensions, jar_radius, jar_height and gumball_radius  
    
    gumball_approximation: Float Float Float -> Nat
    Requires:
    Measurement can never be a negative value 
        jar_radius > 0.0
        jar_height > 0.0
        gumball_radius > 0.0
    
    Examples: 
    gumball_approximation(10.0, 10.0, 1.0) => 480
    gumball_approximation(25554.0, 25554.0, 25554.0) => 0
    '''
    p_density = 0.64 
    v_jar = math.pi * (jar_radius ** 2) * jar_height
    v_gumball = 4/3 * math.pi * (gumball_radius ** 3)
    n_gumball = round((p_density * v_jar) / v_gumball)
    return n_gumball