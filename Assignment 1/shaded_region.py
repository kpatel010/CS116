import math 

def shaded_region(r, d):
    '''
    Returns the area of the overlapping portion of two congruent circles
    using the radius(r) of the circle and the distance(d) between the two
    circles 
    
    shaded_region: Float Float -> Float 
    Requires:
    Measurement can never be a negative value nor zero
        0.0 < d < 2r
        0.0 < r 
        
    Examples:
        shaded_region(2.0, 1.0) => 8.608436900118837
        shaded_region(4331.0, 4331.0) => 23041219.55220537
    '''
    half_length = d / 2
    height_shaded = math.sqrt((r ** 2) - (half_length ** 2))
    inner_angle = (math.asin(height_shaded / r)) * (180 / math.pi)
    smaller_area = (math.pi * (r ** 2) * (inner_angle / 360)) - \
                   (1/2 * half_length * height_shaded)
    final_area = 4 * smaller_area 
    return final_area