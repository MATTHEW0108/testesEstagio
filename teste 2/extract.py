import tabula as tb
import pandas as pd

file = "anexo1.pdf"

def convert(arq):
    arquivo = tb.read_pdf(arq, pages="all", encoding = 'latin-1')
    tb.convert_into(arq, "anexocsv.csv", output_format="csv", pages="all")

def replaceData(csv):
    r = pd.read_csv(csv, encoding = 'latin-1')
    r['OD'] = r['OD'].replace({'OD' : 'Seg. Odontológica'})
    r['AMB'] = r['AMB'].replace({'AMB' : 'Seg. Ambulatorial'})
    r.to_csv("AnexoConvertido.csv", index = False)

convert(file)
replaceData("anexocsv.csv")

