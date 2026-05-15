

rente = input( "Rente p.a.: " )
rente = float( rente )
saldo = input( "Lånesum: " )
saldo = float( saldo )
terminsum = input( "Terminbeløp: " )
terminsum = float( terminsum )
mnd = 0

while saldo > 0:
    saldo += saldo*(rente/100)/12
    saldo -= terminsum
    mnd += 1
    print( f"Månad {mnd} Saldo: {saldo} kr." )


