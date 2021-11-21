# Celestia Asteroid Generator
# 
# Copyright (c) 2021 NE-401
#
# This software is released under the MIT License.
# http://opensource.org/licenses/mit-license.php
#

import math,random,os
from decimal import Decimal as dec

def isfloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False
        

def get_period(StarMass,SMA):
    v_G=6.6725985e-11
    v_meter=float(SMA)*149597870691.0
    v_mass=float(StarMass)*1.98894729428839e30
    
    return (2 * math.pi * math.sqrt((v_meter**3)/(v_G * v_mass))) / 3.15581e7


def gen_asteroids(Fname,StarName,StarMass,NumofAsteroids,MinRadius,MaxRadius,MinSMA,MaxSMA,MaxEccentricity):
    print("--------------- Properties ---------------")
    print("File name: {0}".format(Fname))
    print("Star name: {0}".format(StarName))
    print("Star mass: {0} Solar mass".format(StarMass))
    print("Number of Asteroids: {0}".format(NumofAsteroids))
    print("Radius range: {0} ~ {1} km".format(MinRadius,MaxRadius))
    print("Semi-Major Axis range: {0} ~ {1} AU".format(MinSMA,MaxSMA))
    print("Eccentricity range: {0} ~ {1}".format(0.000,MaxEccentricity))
    print("------------------------------------------")

    mesh=('asteroid.cms','bacchus.cmod','castalia.cmod','epimetheus.cmod','golevka.cmod','janus.cmod','ky26.cmod','pandora.cmod','proteus.cmod','roughsphere.cms')
    
    with open(Fname+".ssc","w",encoding="utf-8") as f:
        for n in range(0,int(NumofAsteroids)):
            SMA=random.uniform(float(MinSMA),float(MaxSMA))
            f.write("# Asteroid No.{0}\n".format(n+1))
            f.write("\"{0} A-{1}\" \"{2}\"\n".format(StarName,int(n+1),StarName))
            f.write("{\n")
            f.write("\tClass \"asteroid\"\n")
            f.write("\tTexture \"asteroid.*\"\n")
            f.write("\tRadius {:.3f}\n".format(random.uniform(MinRadius,MaxRadius)))
            f.write("\tMesh \"{0}\"\n\n".format(random.choice(mesh)))
        
            f.write("\tEllipticalOrbit {\n")
            f.write("\t\tPeriod\t\t\t{0}\n".format(get_period(StarMass,SMA)))
            f.write("\t\tSemiMajorAxis\t\t{0}\n".format(SMA))
            f.write("\t\tEccentricity\t\t{:.5f}\n".format(random.uniform(0.0,MaxEccentricity)))
            f.write("\t\tInclination\t\t{:.3f}\n".format(random.uniform(-15.0,15.0)))
            f.write("\t\tAscendingNode\t\t{:.3f}\n".format(random.uniform(0.0,360.00)))
            f.write("\t\tArgOfPericenter\t\t{:.3f}\n".format(random.uniform(0.0,360.00)))
            f.write("\t\tMeanAnomaly\t\t{:.3f}\n".format(random.uniform(0.0,360.00)))
            f.write("\t}\n\n")
        
            f.write("\tRotationPeriod\t\t{:.3f}\n".format(random.uniform(1.5,8.0)))
            f.write("\tObliquity\t\t{:.3f}\n".format(random.uniform(0.0,360.0)))
            f.write("\tEquatorAscendingNode\t{:.3f}\n".format(random.uniform(0.0,360.0)))
            f.write("\tAlbedo\t\t\t{:.3f}\n".format(random.uniform(0.1,0.5)))
        
            f.write("}\n\n")
            
            print("Asteroid No.{0} generated successfully!".format(n+1))

        
def main():
    # Variables...
    # v_Fname: File name
    # v_StarName: Name of Star
    # v_StarMass: Mass of Star[Solar Mass]
    # v_NumofAsteroids: Number of asteroids create
    # v_MaxEccentricity: Maximum Eccentricity
    # v_MinSMA: Minimum value of Semi-Major Axis[Astronomical Unit]
    # v_MaxSMA: Maximum value of Semi-Major Axis[Astronomical Unit]
    # v_MaxRadius: Maximum radius[km]

    print("Celestia Asteroid belt generator.")

    # Input file name
    while True:
        print("File name(without .ssc extension): ",end="")
        v_Fname=input()
        
        if len(v_Fname) > 0:
            break
        else:
            print("File name must be at least 1 character.")

    # File already exists?
    if os.path.exists(v_Fname+".ssc"):
        while True:
            print("File {0} exists. Do you want overwrite it? [y/N]: ".format(v_Fname+".ssc"),end="")
            f=str(input())
            
            if f == "y" or f == "Y":
                break
            elif f == "n" or f == "N":
                print("Exit the program.")
                exit(0)
                
    # Input star name
    while True:
        print("Central star name: ",end="")
        v_StarName=input()

        if len(v_StarName) > 0:
            break
        else:
            print("Star name must be at least 1 character.")

    # Input Central Star Mass.
    while True:
        print("Central star mass[Solar mass]: ",end="")
        v_StarMass=input()
    
        if isfloat(v_StarMass) and dec(v_StarMass) > dec('0.0'):
            break
        else:
            print("Input rule: ^[0-9]+\.[0-9]+ ")

    # Input Number of Asteroids.
    # Asteroid Limit
    AsteroidLimit=65535
    while True:
        print("Number of Asteroids: ",end="")
        v_NumofAsteroids=input()
        
        if v_NumofAsteroids.isnumeric() and int(v_NumofAsteroids) > 0 and int(v_NumofAsteroids) <= AsteroidLimit:
            break
        else:
            print("Number must be 1~{0}.".format(AsteroidLimit))

    # Minimum Radius[km]
    v_MinRadius=0.850

    # Maximum Radius[km]
    v_MaxRadius=150.00
    
    # Input Minimum Semi-Major Axis[AU].
    while True:
        print("Minimum Semi-Major Axis[AU]: ",end="")
        v_MinSMA=input()
        
        if isfloat(v_MinSMA) and dec(v_MinSMA) > dec(0.0):
            break
        else:
            print("Minimum Semi-Major Axis must be >0.")
    
    # Input Maximum Semi-Major Axis[AU].
    while True:
        print("Maximum Semi-Major Axis[AU]: ",end="")
        v_MaxSMA=input()
        
        if isfloat(v_MaxSMA) and dec(v_MaxSMA) > dec(0.0):
            if v_MaxSMA > v_MinSMA:
                break
            else:
                print("Input Error: Maximum SMA < Minimum SMA.")
        else:
            print("Maximum Semi-Major Axis must be >0.")
    
    # Maximum Eccentricity
    v_MaxEccentricity=0.4

    gen_asteroids(v_Fname,v_StarName,v_StarMass,v_NumofAsteroids,v_MinRadius,v_MaxRadius,v_MinSMA,v_MaxSMA,v_MaxEccentricity)

if __name__ == "__main__":
    main()
    
