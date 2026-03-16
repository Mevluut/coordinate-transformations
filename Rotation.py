print("\n1ST FUCTİON:\n")
###########FUNCTİON 1##########
import numpy as np
#vecs=vektör koordinatları , nang=açı , nax=eksen
def rotation(vecs, ang, ax):
#koordinatları , matris formunda ve yan yana yazdık , açıyı radyandan dereceye çevirdik , cos ve sin değerlerini aldık ;
    vecs = np.array(vecs).flatten()
    ang = np.radians(ang)
    c = np.cos(ang)
    s = np.sin(ang)
    if ax == 1:
        R = np.array([
            [1, 0, 0],
            [0, c, s],
            [0, -s, c]
        ])
    elif ax == 2:
        R = np.array([
            [c, 0, -s],
            [0, 1, 0],
            [s, 0, c]
        ])
    elif ax == 3:
        R = np.array([
            [c, s, 0],
            [-s, c, 0],
            [0, 0, 1]
        ])
    else:
        raise ValueError("Axis must be 1 (X), 2 (Y), or 3 (Z)")
    
    svec = np.dot(R, vecs)

    return svec

x = float(input("X Coordinate: "))
y = float(input("Y Coordinate: "))
z = float(input("Z Coordinate: "))
vecs = np.array([[x], [y], [z]]) 


ax = int(input("Selected Axis => 1=X, 2=Y, 3=Z: "))
ang = float(input("Angle: "))

#SVEC= döndürülen vektör ;
svec= rotation(vecs, ang, ax)
print("Rotated vector:{}".format(svec))




print("\n2ND FUCTİON:\n")
#########FUNCTİON 2##########

#vecs=vektör koordinatları , nang=açı , nax=eksen => n=döndürme sayısı ;
def mainrot(vecs, nang, nax):
#koordinatları , matris formunda ve yan yana yazdık , açıyı radyandan dereceye çevirdik , cos ve sin değerlerini aldık ;
    vecs = np.array(vecs).flatten()
    nangle = np.radians(nang)
    c = np.cos(nangle)
    s = np.sin(nangle)
    
    if nax == 1:
        R = np.array([
            [1, 0, 0],
            [0, c, s],
            [0, -s, c]
        ])
    elif nax == 2:
        R = np.array([
            [c, 0, -s],
            [0, 1, 0],
            [s, 0, c]
        ])
    elif nax == 3:
        R = np.array([
            [c, s, 0],
            [-s, c, 0],
            [0, 0, 1]
        ])
    
    svec = (R @ vecs).reshape(3, 1)
    return svec, R

#üstte yaptıklarımızı main fonksiyonunda çağırdık ;
def main():
    x = int(input("X: "))
    y = int(input("Y: "))
    z = int(input("Z: "))
    
    vecs = np.array([x, y, z])
    
    n = int(input("Rotation number:"))
    
    print("\nStarter Vector: [{x}, {y}, {z}]".format(x=x, y=y, z=z))

#sırayla rotasyon sayısı kadar eksen ve açı bilgilerini alıp rotasyon matrisini ve yeni vektörü hesapladık ;
    for i in range(n):
        nax = int(input("\nSelected Axis => 1,2 or 3: ".format()))
        nang = float(input("Angle: "))
        
        svec, R = mainrot(vecs, nang, nax)
        print("\nRotation vectors:".format())
        print(R)
        #nvec=mainrot(vecs,nang,nax)        
        vecs = svec.flatten()
#başlangıç ve sonuç vektörümüzü yazdırdık ;
    print(f"\nnvec: [{svec[0][0]}, {svec[1][0]:}, {svec[2][0]}]")

main()