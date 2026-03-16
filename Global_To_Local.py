import math
import numpy as np
# Bu fonksiyon(global2local), xyz2blh fonksiyonundan gelen değerleri kullanarak global ellipsoidal sistemden lokal ellipsoidal sisteme dönüşüm yapar.
def global2local(P, R):
     # Gözlem noktasının ellipsoidal koordinatları (xyz2blh'den gelen değerler)
    phi = 47.0  # Enlem (derece)
    lam = 15.0  # Boylam (derece)
    
    # Radyana çevir
    phi_rad = math.radians(phi)
    lam_rad = math.radians(lam)
    
    # Global Kartezyen fark vektörü (ΔT = P - R) *kitaptaki bilgilerden*
    delta_T = P - R
    
    # Dönüşüm matrisi (A) > kitapta verilen A matrisinin transpozu(ya da tersi) aslında 
    sin_phi = math.sin(phi_rad)
    cos_phi = math.cos(phi_rad)
    sin_lam = math.sin(lam_rad)
    cos_lam = math.cos(lam_rad)
    
    A = np.array([
        [-sin_phi * cos_lam,  -sin_phi * sin_lam,   cos_phi],
        [-sin_lam,             cos_lam,              0      ],
        [ cos_phi * cos_lam,   cos_phi * sin_lam,   sin_phi]
    ])
    
    # Lokal Kartezyen koordinatlara dönüştür (Δr = A × ΔT)
    delta_r = A @ delta_T
    x_north = delta_r[0]  # Kuzey için delta_r'ın ilk bileşeni  
    x_east = delta_r[1]   # Doğu için delta_r'ın ikinci bileşeni
    x_up = delta_r[2]     # Yukarı için delta_r'ın üçüncü bileşeni
    # Polar koordinatlara çevir
    s = math.sqrt(x_north**2 + x_east**2 + x_up**2)  # Slant range
    azim = math.degrees(math.atan2(x_east, x_north))  # Azimut açısı
    if azim < 0:
        azim += 360  # Azimutu 0-360 derece aralığına getir
    zen = math.degrees(math.acos(x_up / s))  # Zenit açısı 
    if zen < 0:
        zen += 180  # Zenit açısını 0-180 derece aralığına getir
    r = s  # Slant range
    return azim, zen, r

# Test değerleri **R için xyz2blhin inputları kullanıldı . P için ise random değerler verildi** . değerleri değiştirerek farklı sonuçlar elde edebiliriz. 
P = np.array([4500000.0, 1200000.0, 4700000.0])
R = np.array([4210520.621, 1128205.600, 4643227.496])
azim, zen, r = global2local(P, R)
print("Azimuth angle = {} degree".format(azim))
print("Zenith angle = {} degree".format(zen))
print("Slant range = {} meters".format(r))