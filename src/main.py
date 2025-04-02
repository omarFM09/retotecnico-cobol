import csv

def leer_csv(ruta):
    with open(ruta, mode='r', encoding='utf-8-sig') as file:  # Añade encoding
        return list(csv.DictReader(file, delimiter=';'))  # Usa ; como delimitador

def generar_reporte(transacciones):
    balance = 0.0
    mayor_monto = 0.0
    conteo = {'Crédito': 0, 'Débito': 0}

    for t in transacciones:
        monto = float(t['monto'])
        if t['tipo'] == 'Crédito':  # Asegúrate de que coincida con el CSV
            balance += monto
            conteo['Crédito'] += 1
        else:
            balance -= monto
            conteo['Débito'] += 1
        
        if monto > mayor_monto:
            mayor_monto = monto
            id_mayor = t['id']

    print(f"\nReporte de Transacciones\n{'-'*45}")
    print(f"Balance Final: {balance:.2f}")
    print(f"Transacción de Mayor Monto: ID {id_mayor} - {mayor_monto:.2f}")
    print(f"Conteo: Crédito: {conteo['Crédito']}, Débito: {conteo['Débito']}")

if __name__ == "__main__":
    transacciones = leer_csv("../data/transacciones.csv")
    generar_reporte(transacciones)