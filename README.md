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
corrNetwork.bat ...
```

## Filter correlation scores

1. Positive and negative values

```bash
awk -F ',' '{if ($3 >= 0){print $0}}' PESA_p2q_DigPar_woPos_Correlations.pearson.csv > PESA_p2q_DigPar_woPos_Correlations.pearson.pos.csv
awk -F ',' '{if ($3 < 0){print $0}}' PESA_p2q_DigPar_woPos_Correlations.pearson.csv > PESA_p2q_DigPar_woPos_Correlations.pearson.neg.csv
```

2. Filter by score value

```bash
awk -F ',' '{if ($3 >= 0.6){print $0}}' PESA_p2q_DigPar_woPos_Correlations.pearson.pos.csv > PESA_p2q_DigPar_woPos_Correlations.pearson.pos.thr_06.csv
```

3. Delete minus (absolute value)
```bash
sed 's/\,\-/\,/' PESA_p2q_DigPar_woPos_Correlations.pearson.neg.csv > PESA_p2q_DigPar_woPos_Correlations.pearson.neg.abs.csv
```

