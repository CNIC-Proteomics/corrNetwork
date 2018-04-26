# Correlation Network: perturbation analysis

## Clone repository

```bash
git clone https://github.com/jmrodriguezc/corrNetwork.git
```

or
```bash
wget https://github.com/jmrodriguezc/corrNetwork/archive/master.zip
```

## Execute method

```bash
python correlation_network.py -i data/PESA_V1_Zq.xlsx -o data/PESA_V1.corr_net.pearson.csv
python correlation_network.py -i data/PESA_V1_Zq.xlsx -o data/PESA_V1.corr_net.kendall.csv -m kendall
python correlation_network.py -i data/PESA_V1_Zq.xlsx -o data/PESA_V1.corr_net.spearman.csv -m spearman
```

or

```bash
Note: under construction
corrNetwork.bat ...

```
