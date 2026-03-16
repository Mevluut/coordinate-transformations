import math
def xyz2blh(x, y, z, ell):
    #Cartesian (X,Y,Z) → Ellipsoidal conversion.
    
    # Ellipsoidal parameters
    if ell == 1:  # GRS80
        a = 6378137.0
        inv_flattening = 298.257222101
    elif ell == 2:  # WGS84
        a = 6378137.0
        inv_flattening = 298.257223563
    elif ell == 3:  # PZ-90.02
        a = 6378136.0
        inv_flattening = 298.257839303
    else:
        print("Ellipsoid must be 1 , 2 or 3!")
        return None, None, None
    # Calculate flattening and eccentricity
    flattening = 1 / inv_flattening
    eccentiricity =math.sqrt(2 * flattening - flattening**2)
    
    # Ellipsoidal Longitude
    l = math.degrees(math.atan2(y, x))
   
    # XY Plane Distance
    p = math.sqrt(x**2 + y**2)
   
    # Ellipsoidal Latitude / before iteration
    phi = math.atan(z / (p * (1 - (eccentiricity**2))))
   
    # İteration to calculate phi angle
    for i in range(2):
        # N: Radius of curvature in the prime vertical
        N = a / math.sqrt(1 - (eccentiricity**2) * math.sin(phi)**2)
        
        # Ellipsoidal Height
        h = p / math.cos(phi) - N
        
        # New phi calculation/Ellipsoidal Latitude
        phi_new= math.atan((z / p) / (1 - (eccentiricity**2) * N / (N + h)))
        
        #if the difference is less than 10^-8, break the loop
        if abs(math.degrees(phi_new - phi)) < 10**-8:
            phi = phi_new
            break
    #Ellipsoidal Latitude/after iteration
    b = math.degrees(phi)
    return b, l, h
# Main Program
print("CARTESİAN COORDİNATES => GEODETİC COORDİNATES")

#inputs are : x=4210520.621 , y=1128205.600 , z=4643227.496 (meters) , ellipsoid=1(GRS80)
#Input Cartesian Coordinates
print("\nCartesian Cordinates(m):")
x = float(input("X = "))
y = float(input("Y = "))
z = float(input("Z = "))

#Select Ellipsoid
print("\nSelect the Ellipsoid:")
print("1 - GRS80")
print("2 - WGS84")
print("3 - PZ-90.02")
ell = int(input("Selected ellipsoid: "))
b, l, h = xyz2blh(x, y, z, ell)

#Output Geodetic Coordinates
print("Geodetic Coordinates:")
print("Ellipsoidal latitude = {:.1f}°".format(b))
print("Ellipsoidal longitude = {:.1f}°".format(l))
print("Ellipsoidal Height  = {:.1f} m".format(h))
