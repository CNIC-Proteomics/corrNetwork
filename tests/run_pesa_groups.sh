#!/bin/bash


python correlation_network.py -i "S:\U_Proteomica\PROYECTOS\PESA_omicas\Results_tables_V1_V2\Con_fraccionamiento\Zq\Signature_proteins_JM.xlsx" -o "S:\U_Proteomica\PROYECTOS\PESA_omicas\Results_tables_V1_V2\Con_fraccionamiento\Zq\Signature_proteins_JM.pearson.vs_all.csv" -t

python correlation_network.py -i "S:\U_Proteomica\PROYECTOS\PESA_omicas\Results_tables_V1_V2\Con_fraccionamiento\Zq\Signature_proteins_JM.xlsx" -o "S:\U_Proteomica\PROYECTOS\PESA_omicas\Results_tables_V1_V2\Con_fraccionamiento\Zq\Signature_proteins_JM.pearson.by_group.csv" -t -gr "V1,V2"



