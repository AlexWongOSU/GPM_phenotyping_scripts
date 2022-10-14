#!/usr/bin/python3

"""docstring goes here"""


# Definitions of treatments
CNTL = "Control"
SHAM = "SHAM 100 ug/mL"
AZX1 = "Azoxystrobin 10 ug/mL"
BOS1 = "Boscalid 1 ug/mL"
BOS2 = "Boscalid 10 ug/mL"
BOS3 = "Boscalid 100 ug/mL"
FLU1 = "Fluopyram 1 ug/mL"
FLU2 = "Fluopyram 10 ug/mL"
FLU3 = "Fluopyram 100 ug/mL"
MCB1 = "Myclobutanil 25 ug/mL"
MCB2 = "Myclobutanil 250 ug/mL"
MCB3 = "Myclobutanil 2500 ug/mL"
TEB1 = "Tebuconazole 25 ug/mL"
TEB2 = "Tebuconazole 250 ug/mL"
TEB3 = "Tebuconazole 2500 ug/mL"
DFC1 = "Difenoconazole 25 ug/mL"
DFC2 = "Difenoconazole 250 ug/mL"
DFC3 = "Difenoconazole 2500 ug/mL"
FTF1 = "Flutriafol 25 ug/mL"
FTF2 = "Flutriafol 250 ug/mL"
FTF3 = "Flutriafol 2500 ug/mL"
QXF1 = "Quinoxyfen 0.01 ug/mL"
QXF2 = "Quinoxyfen 0.1 ug/mL"
QXF3 = "Quinoxyfen 1 ug/mL"


# maps of treatment blocks
def get_treatments(plate, block):
    """docstring goes here"""
    if plate == "plate1a":
        # Isolates: LH1, ALV4CH-B
        treatments = [
            CNTL, CNTL, CNTL, CNTL,
            SHAM, SHAM, SHAM, SHAM,
            BOS1, BOS1, BOS1, BOS1,
            AZX1, AZX1, AZX1, AZX1,
            BOS2, BOS2, BOS2, BOS2,
            BOS3, BOS3, BOS3, BOS3,
            FLU2, FLU2, FLU2, FLU2,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            DFC2, DFC2, DFC2, DFC2,
            FTF1, FTF1, FTF1, FTF1,
            FTF2, FTF2, FTF2, FTF2,
            MCB1, MCB1, MCB1, MCB1,
            FTF3, FTF3, FTF3, FTF3,
            MCB2, MCB2, MCB2, MCB2,
            MCB3, MCB3, MCB3, MCB3,
            TEB2, TEB2, TEB2, TEB2,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            QXF1, QXF1, QXF1, QXF1,
            QXF3, QXF3, QXF3, QXF3,
            QXF2, QXF2, QXF2, QXF2,
        ]
    elif plate == "plate1b":
        # Isolates: LH1, MEN8B, ALV4CH-B
        treatments = [
            TEB1, TEB1, TEB1, TEB1,
            TEB2, TEB2, TEB2, TEB2,
            CNTL, CNTL, CNTL, CNTL,
            TEB3, TEB3, TEB3, TEB3,
            SHAM, SHAM, SHAM, SHAM,
            AZX1, AZX1, AZX1, AZX1,
            FTF2, FTF2, FTF2, FTF2,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            QXF1, QXF1, QXF1, QXF1,
            QXF3, QXF3, QXF3, QXF3,
            QXF2, QXF2, QXF2, QXF2,
            BOS1, BOS1, BOS1, BOS1,
            BOS2, BOS2, BOS2, BOS2,
            DFC1, DFC1, DFC1, DFC1,
            BOS3, BOS3, BOS3, BOS3,
            DFC2, DFC2, DFC2, DFC2,
            DFC3, DFC3, DFC3, DFC3,
            FLU2, FLU2, FLU2, FLU2,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            MCB2, MCB2, MCB2, MCB2,
        ]
    elif plate == "plate2a":
        # Isolates: SC4SY-B, MICV3
        treatments = [
            TEB1, TEB1, TEB1, TEB1,
            TEB2, TEB2, TEB2, TEB2,
            MCB1, MCB1, MCB1, MCB1,
            TEB3, TEB3, TEB3, TEB3,
            MCB2, MCB2, MCB2, MCB2,
            MCB3, MCB3, MCB3, MCB3,
            QXF2, QXF2, QXF2, QXF2,
            QXF1, QXF1, QXF1, QXF1,
            QXF3, QXF3, QXF3, QXF3,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            DFC2, DFC2, DFC2, DFC2,
            BOS1, BOS1, BOS1, BOS1,
            BOS2, BOS2, BOS2, BOS2,
            FTF1, FTF1, FTF1, FTF1,
            BOS3, BOS3, BOS3, BOS3,
            FTF2, FTF2, FTF2, FTF2,
            FTF3, FTF3, FTF3, FTF3,
            FLU2, FLU2, FLU2, FLU2,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            CNTL, CNTL, CNTL, CNTL,
            AZX1, AZX1, AZX1, AZX1,
            SHAM, SHAM, SHAM, SHAM,
        ]
    elif plate == "plate2b":
        # Isolates: SC4SY-B, MICV3
        treatments = [
            TEB1, TEB1, TEB1, TEB1,
            TEB2, TEB2, TEB2, TEB2,
            QXF1, QXF1, QXF1, QXF1,
            TEB3, TEB3, TEB3, TEB3,
            QXF2, QXF2, QXF2, QXF2,
            QXF3, QXF3, QXF3, QXF3,
            BOS2, BOS2, BOS2, BOS2,
            BOS1, BOS1, BOS1, BOS1,
            BOS3, BOS3, BOS3, BOS3,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            DFC2, DFC2, DFC2, DFC2,
            MCB1, MCB1, MCB1, MCB1,
            MCB2, MCB2, MCB2, MCB2,
            CNTL, CNTL, CNTL, CNTL,
            MCB3, MCB3, MCB3, MCB3,
            SHAM, SHAM, SHAM, SHAM,
            AZX1, AZX1, AZX1, AZX1,
            FTF2, FTF2, FTF2, FTF2,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            FLU2, FLU2, FLU2, FLU2,
        ]
    elif plate == "plate3a":
        # Isolate: DDO-ME-2, RMT2A
        treatments = [
            MCB1, MCB1, MCB1, MCB1,
            MCB2, MCB2, MCB2, MCB2,
            FTF1, FTF1, FTF1, FTF1,
            MCB3, MCB3, MCB3, MCB3,
            FTF2, FTF2, FTF2, FTF2,
            FTF3, FTF3, FTF3, FTF3,
            TEB2, TEB2, TEB2, TEB2,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            DFC2, DFC2, DFC2, DFC2,
            QXF1, QXF1, QXF1, QXF1,
            QXF2, QXF2, QXF2, QXF2,
            CNTL, CNTL, CNTL, CNTL,
            QXF3, QXF3, QXF3, QXF3,
            SHAM, SHAM, SHAM, SHAM,
            AZX1, AZX1, AZX1, AZX1,
            BOS2, BOS2, BOS2, BOS2,
            BOS1, BOS1, BOS1, BOS1,
            BOS3, BOS3, BOS3, BOS3,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            FLU2, FLU2, FLU2, FLU2,
        ]
    elif plate == "plate3b":
        # Isolate: DDO-ME-2, RMT2A
        treatments = [
            CNTL, CNTL, CNTL, CNTL,
            SHAM, SHAM, SHAM, SHAM,
            QXF1, QXF1, QXF1, QXF1,
            AZX1, AZX1, AZX1, AZX1,
            QXF2, QXF2, QXF2, QXF2,
            QXF3, QXF3, QXF3, QXF3,
            FLU2, FLU2, FLU2, FLU2,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            DFC2, DFC2, DFC2, DFC2,
            BOS1, BOS1, BOS1, BOS1,
            BOS2, BOS2, BOS2, BOS2,
            TEB1, TEB1, TEB1, TEB1,
            BOS3, BOS3, BOS3, BOS3,
            TEB2, TEB2, TEB2, TEB2,
            TEB3, TEB3, TEB3, TEB3,
            FTF2, FTF2, FTF2, FTF2,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            MCB2, MCB2, MCB2, MCB2,
        ]
    elif plate == "plate4a":
        # Isolate: GAT1, ADPN
        treatments = [
            QXF1, QXF1, QXF1, QXF1,
            QXF2, QXF2, QXF2, QXF2,
            FLU1, FLU1, FLU1, FLU1,
            QXF3, QXF3, QXF3, QXF3,
            FLU2, FLU2, FLU2, FLU2,
            FLU3, FLU3, FLU3, FLU3,
            BOS2, BOS2, BOS2, BOS2,
            BOS1, BOS1, BOS1, BOS1,
            BOS3, BOS3, BOS3, BOS3,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            DFC2, DFC2, DFC2, DFC2,
            FTF1, FTF1, FTF1, FTF1,
            FTF2, FTF2, FTF2, FTF2,
            TEB1, TEB1, TEB1, TEB1,
            FTF3, FTF3, FTF3, FTF3,
            TEB2, TEB2, TEB2, TEB2,
            TEB3, TEB3, TEB3, TEB3,
            SHAM, SHAM, SHAM, SHAM,
            CNTL, CNTL, CNTL, CNTL,
            AZX1, AZX1, AZX1, AZX1,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            MCB2, MCB2, MCB2, MCB2,
        ]
    elif plate == "plate4b":
        # Isolate: ADPN
        treatments = [
            MCB1, MCB1, MCB1, MCB1,
            MCB2, MCB2, MCB2, MCB2,
            FLU1, FLU1, FLU1, FLU1,
            MCB3, MCB3, MCB3, MCB3,
            FLU2, FLU2, FLU2, FLU2,
            FLU3, FLU3, FLU3, FLU3,
            FTF2, FTF2, FTF2, FTF2,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            CNTL, CNTL, CNTL, CNTL,
            AZX1, AZX1, AZX1, AZX1,
            SHAM, SHAM, SHAM, SHAM,
            QXF1, QXF1, QXF1, QXF1,
            QXF2, QXF2, QXF2, QXF2,
            DFC1, DFC1, DFC1, DFC1,
            QXF3, QXF3, QXF3, QXF3,
            DFC2, DFC2, DFC2, DFC2,
            DFC3, DFC3, DFC3, DFC3,
            BOS2, BOS2, BOS2, BOS2,
            BOS1, BOS1, BOS1, BOS1,
            BOS3, BOS3, BOS3, BOS3,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            TEB2, TEB2, TEB2, TEB2,
        ]
    elif plate == "plate5a":
        # Isolates: KRAE1B, NAPA02-T
        treatments = [
            FTF1, FTF1, FTF1, FTF1,
            FTF2, FTF2, FTF2, FTF2,
            QXF1, QXF1, QXF1, QXF1,
            FTF3, FTF3, FTF3, FTF3,
            QXF2, QXF2, QXF2, QXF2,
            QXF3, QXF3, QXF3, QXF3,
            TEB2, TEB2, TEB2, TEB2,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            FLU2, FLU2, FLU2, FLU2,
            BOS1, BOS1, BOS1, BOS1,
            BOS2, BOS2, BOS2, BOS2,
            CNTL, CNTL, CNTL, CNTL,
            BOS3, BOS3, BOS3, BOS3,
            SHAM, SHAM, SHAM, SHAM,
            AZX1, AZX1, AZX1, AZX1,
            MCB2, MCB2, MCB2, MCB2,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            DFC2, DFC2, DFC2, DFC2,
        ]
    elif plate == "plate5b":
        # Isolates: KRAE1B, NAPA02-T
        treatments = [
            TEB1, TEB1, TEB1, TEB1,
            TEB2, TEB2, TEB2, TEB2,
            DFC1, DFC1, DFC1, DFC1,
            TEB3, TEB3, TEB3, TEB3,
            DFC2, DFC2, DFC2, DFC2,
            DFC3, DFC3, DFC3, DFC3,
            BOS2, BOS2, BOS2, BOS2,
            BOS1, BOS1, BOS1, BOS1,
            BOS3, BOS3, BOS3, BOS3,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            FTF2, FTF2, FTF2, FTF2,
            QXF1, QXF1, QXF1, QXF1,
            QXF2, QXF2, QXF2, QXF2,
            FLU1, FLU1, FLU1, FLU1,
            QXF3, QXF3, QXF3, QXF3,
            FLU2, FLU2, FLU2, FLU2,
            FLU3, FLU3, FLU3, FLU3,
            MCB2, MCB2, MCB2, MCB2,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            CNTL, CNTL, CNTL, CNTL,
            AZX1, AZX1, AZX1, AZX1,
            SHAM, SHAM, SHAM, SHAM,
        ]
    elif plate == "plate6a":
        # Isolates: R532ST190-1, NAPA05-PB
        treatments = [
            MCB1, MCB1, MCB1, MCB1,
            MCB2, MCB2, MCB2, MCB2,
            FTF1, FTF1, FTF1, FTF1,
            MCB3, MCB3, MCB3, MCB3,
            FTF2, FTF2, FTF2, FTF2,
            FTF3, FTF3, FTF3, FTF3,
            TEB2, TEB2, TEB2, TEB2,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            QXF1, QXF1, QXF1, QXF1,
            QXF3, QXF3, QXF3, QXF3,
            QXF2, QXF2, QXF2, QXF2,
            CNTL, CNTL, CNTL, CNTL,
            SHAM, SHAM, SHAM, SHAM,
            DFC1, DFC1, DFC1, DFC1,
            AZX1, AZX1, AZX1, AZX1,
            DFC2, DFC2, DFC2, DFC2,
            DFC3, DFC3, DFC3, DFC3,
            FLU2, FLU2, FLU2, FLU2,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            BOS1, BOS1, BOS1, BOS1,
            BOS3, BOS3, BOS3, BOS3,
            BOS2, BOS2, BOS2, BOS2,
        ]
    elif plate == "plate6b":
        # Isolates: R532ST190-1, NAPA05-PB
        treatments = [
            MCB1, MCB1, MCB1, MCB1,
            MCB2, MCB2, MCB2, MCB2,
            CNTL, CNTL, CNTL, CNTL,
            MCB3, MCB3, MCB3, MCB3,
            SHAM, SHAM, SHAM, SHAM,
            AZX1, AZX1, AZX1, AZX1,
            DFC2, DFC2, DFC2, DFC2,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            FTF2, FTF2, FTF2, FTF2,
            TEB1, TEB1, TEB1, TEB1,
            TEB2, TEB2, TEB2, TEB2,
            FLU1, FLU1, FLU1, FLU1,
            TEB3, TEB3, TEB3, TEB3,
            FLU2, FLU2, FLU2, FLU2,
            FLU3, FLU3, FLU3, FLU3,
            BOS2, BOS2, BOS2, BOS2,
            BOS1, BOS1, BOS1, BOS1,
            BOS3, BOS3, BOS3, BOS3,
            QXF1, QXF1, QXF1, QXF1,
            QXF3, QXF3, QXF3, QXF3,
            QXF2, QXF2, QXF2, QXF2,
        ]
    elif plate == "plate7a":
        # Isolates: GAT1, PFV-6A
        treatments = [
            QXF1, QXF1, QXF1, QXF1,
            QXF2, QXF2, QXF2, QXF2,
            BOS1, BOS1, BOS1, BOS1,
            QXF3, QXF3, QXF3, QXF3,
            BOS2, BOS2, BOS2, BOS2,
            BOS3, BOS3, BOS3, BOS3,
            FTF2, FTF2, FTF2, FTF2,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            MCB2, MCB2, MCB2, MCB2,
            DFC1, DFC1, DFC1, DFC1,
            DFC2, DFC2, DFC2, DFC2,
            TEB1, TEB1, TEB1, TEB1,
            DFC3, DFC3, DFC3, DFC3,
            TEB2, TEB2, TEB2, TEB2,
            TEB3, TEB3, TEB3, TEB3,
            FLU2, FLU2, FLU2, FLU2,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            CNTL, CNTL, CNTL, CNTL,
            AZX1, AZX1, AZX1, AZX1,
            SHAM, SHAM, SHAM, SHAM,
        ]
    elif plate == "plate7b":
        # Isolates: GAT1, PFV-6A
        treatments = [
            CNTL, CNTL, CNTL, CNTL,
            SHAM, SHAM, SHAM, SHAM,
            QXF1, QXF1, QXF1, QXF1,
            AZX1, AZX1, AZX1, AZX1,
            QXF2, QXF2, QXF2, QXF2,
            QXF3, QXF3, QXF3, QXF3,
            BOS2, BOS2, BOS2, BOS2,
            BOS1, BOS1, BOS1, BOS1,
            BOS3, BOS3, BOS3, BOS3,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            MCB2, MCB2, MCB2, MCB2,
            FLU1, FLU1, FLU1, FLU1,
            FLU2, FLU2, FLU2, FLU2,
            DFC1, DFC1, DFC1, DFC1,
            FLU3, FLU3, FLU3, FLU3,
            DFC2, DFC2, DFC2, DFC2,
            DFC3, DFC3, DFC3, DFC3,
            TEB2, TEB2, TEB2, TEB2,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            FTF2, FTF2, FTF2, FTF2,
        ]
    elif plate == "plate8a":
        # Isolates: HO2, SE-22B
        treatments = [
            BOS1, BOS1, BOS1, BOS1,
            BOS2, BOS2, BOS2, BOS2,
            DFC1, DFC1, DFC1, DFC1,
            BOS3, BOS3, BOS3, BOS3,
            DFC2, DFC2, DFC2, DFC2,
            DFC3, DFC3, DFC3, DFC3,
            FLU2, FLU2, FLU2, FLU2,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            MCB2, MCB2, MCB2, MCB2,
            CNTL, CNTL, CNTL, CNTL,
            SHAM, SHAM, SHAM, SHAM,
            TEB1, TEB1, TEB1, TEB1,
            AZX1, AZX1, AZX1, AZX1,
            TEB2, TEB2, TEB2, TEB2,
            TEB3, TEB3, TEB3, TEB3,
            QXF2, QXF2, QXF2, QXF2,
            QXF1, QXF1, QXF1, QXF1,
            QXF3, QXF3, QXF3, QXF3,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            FTF2, FTF2, FTF2, FTF2,
        ]
    elif plate == "plate8b":
        # Isolates: HO2, SE-22B
        treatments = [
            TEB1, TEB1, TEB1, TEB1,
            TEB2, TEB2, TEB2, TEB2,
            FTF1, FTF1, FTF1, FTF1,
            TEB3, TEB3, TEB3, TEB3,
            FTF2, FTF2, FTF2, FTF2,
            FTF3, FTF3, FTF3, FTF3,
            BOS2, BOS2, BOS2, BOS2,
            BOS1, BOS1, BOS1, BOS1,
            BOS3, BOS3, BOS3, BOS3,
            CNTL, CNTL, CNTL, CNTL,
            AZX1, AZX1, AZX1, AZX1,
            SHAM, SHAM, SHAM, SHAM,
            DFC1, DFC1, DFC1, DFC1,
            DFC2, DFC2, DFC2, DFC2,
            QXF1, QXF1, QXF1, QXF1,
            DFC3, DFC3, DFC3, DFC3,
            QXF2, QXF2, QXF2, QXF2,
            QXF3, QXF3, QXF3, QXF3,
            MCB2, MCB2, MCB2, MCB2,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            FLU2, FLU2, FLU2, FLU2,
        ]
    elif plate == "plate9a":
        # Isolate: CAL3B
        treatments = [
            FTF1, FTF1, FTF1, FTF1,
            FTF2, FTF2, FTF2, FTF2,
            QXF1, QXF1, QXF1, QXF1,
            FTF3, FTF3, FTF3, FTF3,
            QXF2, QXF2, QXF2, QXF2,
            QXF3, QXF3, QXF3, QXF3,
            SHAM, SHAM, SHAM, SHAM,
            CNTL, CNTL, CNTL, CNTL,
            AZX1, AZX1, AZX1, AZX1,
            BOS1, BOS1, BOS1, BOS1,
            BOS3, BOS3, BOS3, BOS3,
            BOS2, BOS2, BOS2, BOS2,
            FLU1, FLU1, FLU1, FLU1,
            FLU2, FLU2, FLU2, FLU2,
            MCB1, MCB1, MCB1, MCB1,
            FLU3, FLU3, FLU3, FLU3,
            MCB2, MCB2, MCB2, MCB2,
            MCB3, MCB3, MCB3, MCB3,
            TEB2, TEB2, TEB2, TEB2,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            DFC2, DFC2, DFC2, DFC2,
        ]
    elif plate == "plate9b":
        # Isolate: CAL3B
        treatments = [
            QXF1, QXF1, QXF1, QXF1,
            QXF2, QXF2, QXF2, QXF2,
            BOS1, BOS1, BOS1, BOS1,
            QXF3, QXF3, QXF3, QXF3,
            BOS2, BOS2, BOS2, BOS2,
            BOS3, BOS3, BOS3, BOS3,
            MCB2, MCB2, MCB2, MCB2,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            TEB2, TEB2, TEB2, TEB2,
            DFC1, DFC1, DFC1, DFC1,
            DFC2, DFC2, DFC2, DFC2,
            FLU1, FLU1, FLU1, FLU1,
            DFC3, DFC3, DFC3, DFC3,
            FLU2, FLU2, FLU2, FLU2,
            FLU3, FLU3, FLU3, FLU3,
            FTF2, FTF2, FTF2, FTF2,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            CNTL, CNTL, CNTL, CNTL,
            AZX1, AZX1, AZX1, AZX1,
            SHAM, SHAM, SHAM, SHAM,
        ]
    elif plate == "plate10a":
        # Isolate: MITG2
        treatments = [
            CNTL, CNTL, CNTL, CNTL,
            SHAM, SHAM, SHAM, SHAM,
            FTF1, FTF1, FTF1, FTF1,
            AZX1, AZX1, AZX1, AZX1,
            FTF2, FTF2, FTF2, FTF2,
            FTF3, FTF3, FTF3, FTF3,
            QXF2, QXF2, QXF2, QXF2,
            QXF1, QXF1, QXF1, QXF1,
            QXF3, QXF3, QXF3, QXF3,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            TEB2, TEB2, TEB2, TEB2,
            DFC1, DFC1, DFC1, DFC1,
            DFC2, DFC2, DFC2, DFC2,
            BOS1, BOS1, BOS1, BOS1,
            DFC3, DFC3, DFC3, DFC3,
            BOS2, BOS2, BOS2, BOS2,
            BOS3, BOS3, BOS3, BOS3,
            FLU2, FLU2, FLU2, FLU2,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            MCB2, MCB2, MCB2, MCB2,
        ]
    elif plate == "plate10b":
        # Isolate: MITG2
        treatments = [
            FLU1, FLU1, FLU1, FLU1,
            FLU2, FLU2, FLU2, FLU2,
            DFC1, DFC1, DFC1, DFC1,
            FLU3, FLU3, FLU3, FLU3,
            DFC2, DFC2, DFC2, DFC2,
            DFC3, DFC3, DFC3, DFC3,
            QXF2, QXF2, QXF2, QXF2,
            QXF1, QXF1, QXF1, QXF1,
            QXF3, QXF3, QXF3, QXF3,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            TEB2, TEB2, TEB2, TEB2,
            BOS1, BOS1, BOS1, BOS1,
            BOS2, BOS2, BOS2, BOS2,
            CNTL, CNTL, CNTL, CNTL,
            BOS3, BOS3, BOS3, BOS3,
            SHAM, SHAM, SHAM, SHAM,
            AZX1, AZX1, AZX1, AZX1,
            MCB2, MCB2, MCB2, MCB2,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            FTF2, FTF2, FTF2, FTF2,
        ]
    elif plate == "plate11a":
        # Isolate: BHN
        treatments = [
            DFC1, DFC1, DFC1, DFC1,
            DFC2, DFC2, DFC2, DFC2,
            FTF1, FTF1, FTF1, FTF1,
            DFC3, DFC3, DFC3, DFC3,
            FTF2, FTF2, FTF2, FTF2,
            FTF3, FTF3, FTF3, FTF3,
            QXF2, QXF2, QXF2, QXF2,
            QXF1, QXF1, QXF1, QXF1,
            QXF3, QXF3, QXF3, QXF3,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            MCB2, MCB2, MCB2, MCB2,
            CNTL, CNTL, CNTL, CNTL,
            SHAM, SHAM, SHAM, SHAM,
            TEB1, TEB1, TEB1, TEB1,
            AZX1, AZX1, AZX1, AZX1,
            TEB2, TEB2, TEB2, TEB2,
            TEB3, TEB3, TEB3, TEB3,
            FLU2, FLU2, FLU2, FLU2,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            BOS1, BOS1, BOS1, BOS1,
            BOS3, BOS3, BOS3, BOS3,
            BOS2, BOS2, BOS2, BOS2,
        ]
    elif plate == "plate11b":
        # Isolate: BHN
        treatments = [
            CNTL, CNTL, CNTL, CNTL,
            SHAM, SHAM, SHAM, SHAM,
            BOS1, BOS1, BOS1, BOS1,
            AZX1, AZX1, AZX1, AZX1,
            BOS2, BOS2, BOS2, BOS2,
            BOS3, BOS3, BOS3, BOS3,
            FLU2, FLU2, FLU2, FLU2,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            DFC2, DFC2, DFC2, DFC2,
            QXF1, QXF1, QXF1, QXF1,
            QXF2, QXF2, QXF2, QXF2,
            FTF1, FTF1, FTF1, FTF1,
            QXF3, QXF3, QXF3, QXF3,
            FTF2, FTF2, FTF2, FTF2,
            FTF3, FTF3, FTF3, FTF3,
            MCB2, MCB2, MCB2, MCB2,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            TEB2, TEB2, TEB2, TEB2,
        ]
    elif plate == "plate12a":
        # Isolate: MICV1
        treatments = [
            QXF1, QXF1, QXF1, QXF1,
            QXF2, QXF2, QXF2, QXF2,
            BOS1, BOS1, BOS1, BOS1,
            QXF3, QXF3, QXF3, QXF3,
            BOS2, BOS2, BOS2, BOS2,
            BOS3, BOS3, BOS3, BOS3,
            MCB2, MCB2, MCB2, MCB2,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            DFC2, DFC2, DFC2, DFC2,
            FLU1, FLU1, FLU1, FLU1,
            FLU2, FLU2, FLU2, FLU2,
            CNTL, CNTL, CNTL, CNTL,
            FLU3, FLU3, FLU3, FLU3,
            SHAM, SHAM, SHAM, SHAM,
            AZX1, AZX1, AZX1, AZX1,
            FTF2, FTF2, FTF2, FTF2,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            TEB2, TEB2, TEB2, TEB2,
        ]
    elif plate == "plate12b":
        # Isolate: MICV1
        treatments = [
            QXF1, QXF1, QXF1, QXF1,
            QXF2, QXF2, QXF2, QXF2,
            DFC1, DFC1, DFC1, DFC1,
            QXF3, QXF3, QXF3, QXF3,
            DFC2, DFC2, DFC2, DFC2,
            DFC3, DFC3, DFC3, DFC3,
            MCB2, MCB2, MCB2, MCB2,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            FTF2, FTF2, FTF2, FTF2,
            CNTL, CNTL, CNTL, CNTL,
            SHAM, SHAM, SHAM, SHAM,
            FLU1, FLU1, FLU1, FLU1,
            AZX1, AZX1, AZX1, AZX1,
            FLU2, FLU2, FLU2, FLU2,
            FLU3, FLU3, FLU3, FLU3,
            BOS2, BOS2, BOS2, BOS2,
            BOS1, BOS1, BOS1, BOS1,
            BOS3, BOS3, BOS3, BOS3,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            TEB2, TEB2, TEB2, TEB2,
        ]
    elif plate == "plate13a":
        # Isolate: GAT2
        treatments = [
            DFC1, DFC1, DFC1, DFC1,
            DFC2, DFC2, DFC2, DFC2,
            CNTL, CNTL, CNTL, CNTL,
            DFC3, DFC3, DFC3, DFC3,
            SHAM, SHAM, SHAM, SHAM,
            AZX1, AZX1, AZX1, AZX1,
            FLU2, FLU2, FLU2, FLU2,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            QXF1, QXF1, QXF1, QXF1,
            QXF3, QXF3, QXF3, QXF3,
            QXF2, QXF2, QXF2, QXF2,
            TEB1, TEB1, TEB1, TEB1,
            TEB2, TEB2, TEB2, TEB2,
            BOS1, BOS1, BOS1, BOS1,
            TEB3, TEB3, TEB3, TEB3,
            BOS2, BOS2, BOS2, BOS2,
            BOS3, BOS3, BOS3, BOS3,
            MCB2, MCB2, MCB2, MCB2,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            FTF2, FTF2, FTF2, FTF2,
        ]
    elif plate == "plate13b":
        # Isolate: GAT2
        treatments = [
            MCB1, MCB1, MCB1, MCB1,
            MCB2, MCB2, MCB2, MCB2,
            TEB1, TEB1, TEB1, TEB1,
            MCB3, MCB3, MCB3, MCB3,
            TEB2, TEB2, TEB2, TEB2,
            TEB3, TEB3, TEB3, TEB3,
            BOS2, BOS2, BOS2, BOS2,
            BOS1, BOS1, BOS1, BOS1,
            BOS3, BOS3, BOS3, BOS3,
            CNTL, CNTL, CNTL, CNTL,
            AZX1, AZX1, AZX1, AZX1,
            SHAM, SHAM, SHAM, SHAM,
            DFC1, DFC1, DFC1, DFC1,
            DFC2, DFC2, DFC2, DFC2,
            FLU1, FLU1, FLU1, FLU1,
            DFC3, DFC3, DFC3, DFC3,
            FLU2, FLU2, FLU2, FLU2,
            FLU3, FLU3, FLU3, FLU3,
            QXF2, QXF2, QXF2, QXF2,
            QXF1, QXF1, QXF1, QXF1,
            QXF3, QXF3, QXF3, QXF3,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            FTF2, FTF2, FTF2, FTF2,
        ]
    elif plate == "plate14a":
        # Isolate: MICV3
        treatments = [
            MCB1, MCB1, MCB1, MCB1,
            MCB2, MCB2, MCB2, MCB2,
            BOS1, BOS1, BOS1, BOS1,
            MCB3, MCB3, MCB3, MCB3,
            BOS2, BOS2, BOS2, BOS2,
            BOS3, BOS3, BOS3, BOS3,
            SHAM, SHAM, SHAM, SHAM,
            CNTL, CNTL, CNTL, CNTL,
            AZX1, AZX1, AZX1, AZX1,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            FLU2, FLU2, FLU2, FLU2,
            FTF1, FTF1, FTF1, FTF1,
            FTF2, FTF2, FTF2, FTF2,
            QXF1, QXF1, QXF1, QXF1,
            FTF3, FTF3, FTF3, FTF3,
            QXF2, QXF2, QXF2, QXF2,
            QXF3, QXF3, QXF3, QXF3,
            DFC2, DFC2, DFC2, DFC2,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            TEB2, TEB2, TEB2, TEB2,
        ]
    elif plate == "plate14b":
        # Isolate: MICV3
        treatments = [
            BOS1, BOS1, BOS1, BOS1,
            BOS2, BOS2, BOS2, BOS2,
            FLU1, FLU1, FLU1, FLU1,
            BOS3, BOS3, BOS3, BOS3,
            FLU2, FLU2, FLU2, FLU2,
            FLU3, FLU3, FLU3, FLU3,
            QXF2, QXF2, QXF2, QXF2,
            QXF1, QXF1, QXF1, QXF1,
            QXF3, QXF3, QXF3, QXF3,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            FTF2, FTF2, FTF2, FTF2,
            CNTL, CNTL, CNTL, CNTL,
            SHAM, SHAM, SHAM, SHAM,
            MCB1, MCB1, MCB1, MCB1,
            AZX1, AZX1, AZX1, AZX1,
            MCB2, MCB2, MCB2, MCB2,
            MCB3, MCB3, MCB3, MCB3,
            TEB2, TEB2, TEB2, TEB2,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            DFC2, DFC2, DFC2, DFC2,
        ]
    elif plate == "plate15a":
        # Isolate: E1-101
        treatments = [
            FLU1, FLU1, FLU1, FLU1,
            FLU2, FLU2, FLU2, FLU2,
            DFC1, DFC1, DFC1, DFC1,
            FLU3, FLU3, FLU3, FLU3,
            DFC2, DFC2, DFC2, DFC2,
            DFC3, DFC3, DFC3, DFC3,
            TEB2, TEB2, TEB2, TEB2,
            TEB1, TEB1, TEB1, TEB1,
            TEB3, TEB3, TEB3, TEB3,
            CNTL, CNTL, CNTL, CNTL,
            AZX1, AZX1, AZX1, AZX1,
            SHAM, SHAM, SHAM, SHAM,
            BOS1, BOS1, BOS1, BOS1,
            BOS2, BOS2, BOS2, BOS2,
            QXF1, QXF1, QXF1, QXF1,
            BOS3, BOS3, BOS3, BOS3,
            QXF2, QXF2, QXF2, QXF2,
            QXF3, QXF3, QXF3, QXF3,
            MCB2, MCB2, MCB2, MCB2,
            MCB1, MCB1, MCB1, MCB1,
            MCB3, MCB3, MCB3, MCB3,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            FTF2, FTF2, FTF2, FTF2,
        ]
    elif plate == "plate15b":
        # Isolate: E1-101
        treatments = [
            MCB1, MCB1, MCB1, MCB1,
            MCB2, MCB2, MCB2, MCB2,
            TEB1, TEB1, TEB1, TEB1,
            MCB3, MCB3, MCB3, MCB3,
            TEB2, TEB2, TEB2, TEB2,
            TEB3, TEB3, TEB3, TEB3,
            QXF2, QXF2, QXF2, QXF2,
            QXF1, QXF1, QXF1, QXF1,
            QXF3, QXF3, QXF3, QXF3,
            FTF1, FTF1, FTF1, FTF1,
            FTF3, FTF3, FTF3, FTF3,
            FTF2, FTF2, FTF2, FTF2,
            CNTL, CNTL, CNTL, CNTL,
            SHAM, SHAM, SHAM, SHAM,
            BOS1, BOS1, BOS1, BOS1,
            AZX1, AZX1, AZX1, AZX1,
            BOS2, BOS2, BOS2, BOS2,
            BOS3, BOS3, BOS3, BOS3,
            DFC2, DFC2, DFC2, DFC2,
            DFC1, DFC1, DFC1, DFC1,
            DFC3, DFC3, DFC3, DFC3,
            FLU1, FLU1, FLU1, FLU1,
            FLU3, FLU3, FLU3, FLU3,
            FLU2, FLU2, FLU2, FLU2,
        ]
    return treatments[block]
