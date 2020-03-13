import requests

#Api para recoger datos de cotizaciones de dolar y euro
r = requests.get('http://api.bluelytics.com.ar/v2/latest').json()

oficompra = float(r["oficial"]['value_buy'])
ofiventa = float(r["oficial"]['value_sell'])
soli = float(ofiventa + (ofiventa*0.3))
bluecompra = float(r["blue"]['value_buy'])
blueventa = float(r["blue"]['value_sell'])
eoficompra = float(r["oficial_euro"]['value_buy'])
eofiventa = float(r["oficial_euro"]['value_sell'])
esoli = float(eofiventa + (eofiventa*0.3))
ebluecompra = float(r["blue_euro"]['value_buy'])
eblueventa = float(r["blue_euro"]['value_sell'])
update = str(r["last_update"])


#Impresion de datos
print('   Moneda   | compra | venta | C/Imp. Pais')
print('------------|--------|-------|------------')
print("U$S Oficial | " , '%.2f' %oficompra , "|" , '%.2f' %ofiventa , "|  " , '%.2f' %soli)
print("U$D Blue    | " , '%.2f' %bluecompra , "|" , '%.2f' %blueventa , "|  ")
print("Euro Oficial| " , '%.2f' %eoficompra , "|" , '%.2f' %eofiventa , "|  " , '%.2f' %esoli)
print("Euro Blue   | " , '%.2f' %ebluecompra , "|" , '%.2f' %eblueventa , "|  ")
print('------------|--------|-------|-----------------')
print("Ultima Actualizacion Dia: " + update[:10] + " | Hora: " + update[11:19])
