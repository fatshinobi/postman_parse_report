# Postman parse report
Command Line application to parse endpoints from postman json report and save it as csv, pdf

## System Requirements
  * Python >= 3.10

## Usage
To parse into csv file:
```bash
$ python3.10 main.py csv /home/fat_shinobi/report.json /home/fat_shinobi/api_result.csv
```

To parse into csv file::
```bash
$ python3.10 main.py pdf /home/fat_shinobi/report.json /home/fat_shinobi/api_result.pdf
```
