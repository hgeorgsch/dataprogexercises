# ---
# jupyter:
#   jupytext:
#     default_lexer: ipython3
#     formats: md:myst,ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.0
#   kernelspec:
#     display_name: dataprog
#     language: python
#     name: dataprog
# ---

import pandas as pd
import argparse

def reformatCols( df ):
    df['dato'] = pd.to_datetime(df['TIME_PERIOD'], format='%Y-%m-%d')
    df['kurs'] = df['OBS_VALUE'].str.replace(',', '.')
    df['kurs'] = pd.to_numeric(df['kurs'])
    return df

def currencyCols( df ):
    valutaar = df["BASE_CUR"].unique()
    lst = []
    for valuta in valutaar:
        valdf = df[ df["BASE_CUR"] == valuta ]
        valdf = valdf.reset_index()
        valdf[valuta] = valdf["kurs"]
        valdf = valdf.filter( items= [ "dato", valuta ] )
        lst.append( valdf )
    nydf = lst[0]
    for valdf in lst[1:]:
        nydf = pd.merge( nydf, valdf, on="dato" )
    return nydf

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Konverter valutakursdata.")

    parser.add_argument("infile", type=str, help="Input file.")
    parser.add_argument("outfile", type=str, help="Output file.")
    args = parser.parse_args()

    df = pd.read_csv(args.infile, sep=";")
    df = reformatCols( df )
    mrg = currencyCols( df )
    mrg.to_csv(args.outfile, index=False)
