from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = request.form['nota1'].replace(".0","")
        nota2 = request.form['nota2'].replace(".0","")
        nota3 = request.form['nota3'].replace(".0","")
        asistencia = request.form['asistencia'].replace(".0","")
        #a continuación controlamos que no se dejen espacios en blanco ni tampoco se ingresen letras o símbolos que no correspondan a números.
        if(not nota1.isnumeric()) or (not nota2.isnumeric()) or (not nota3.isnumeric()) or (not asistencia.isnumeric()):
            return render_template('ejercicio1.html', promedioInput="ERROR", estadoInput="Por favor ingresar valores válidos")
        nota1 = float(nota1)
        nota2 = float(nota2)
        nota3 = float(nota3)
        asistencia = float(asistencia)
        #En el ejemplo de las instrucciones los valores ingresados no son valores decimales y por lo tanto
        #las notas solo se considerarán validas si se encuentran entre 10 y 70.
        if (nota1)>70 or (nota1)<10 or (nota2)>70 or (nota2)<10 or (nota3)>70 or (nota3)<10 or (asistencia)>100.0 or asistencia<0.0:
            promedio = "ERROR"
            estado = "Por favor ingresar valores válidos"
        else:
            promedio = (nota1+nota2+nota3)/3
            if asistencia >= 75 and promedio >= 40:
                estado = "APROBADO"
            else:
                estado = "REPROBADO"
        return render_template('ejercicio1.html', nota1Input=nota1, nota2Input=nota2, nota3Input=nota3, asistenciaInput=asistencia, promedioInput=promedio, estadoInput=estado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        #Como en las instrucciones se especifica que los 3 nombres ingresados deben ser diferentes
        #controlamos que ningun nombre ingresado pueda ser igual a otro, pense en controlar la posibilidad
        #de que dos o mas nombres tuviesen la misma cantidad de caracteres, sin embargo, al no estar esta situación
        #contemplada en las instrucciones de la evaluación decidí no hacerlo, aunque ciertamente podría hacerlo.
        if nombre1 == nombre2 or nombre1 == nombre3 or nombre2 == nombre3:
            nombreMasLargo = f'Error'
            numCaracteres = f'Por favor ingresar nombres distintos'
        else:
            lNombre1 = list(nombre1)
            a = len(lNombre1)
            lNombre2 = list(nombre2)
            b = len(lNombre2)
            lNombre3 = list(nombre3)
            c = len(lNombre3)
            listaLongitud = [a, b, c]
            listaLongitud.sort()
            d = listaLongitud[2]
            #a continuación primero controlamos que sean ingresados 3 nombres arrojando un error si a, b o c es 0 (es decir que carecen de caracteres)
            #luego comparamos a, b y c con el valor d, el cual determina al nombre con mayor numero de caracteres.
            if a == 0 or b== 0 or c==0:
                nombreMasLargo = f'Error'
                numCaracteres = f'Por favor no dejar espacios en blanco'
            else:
                if d == a:
                    nombreMasLargo = f'El nombre con mayor cantidad de caracteres es: {nombre1}'
                    numCaracteres = f'El nombre tiene : {a} caracteres'
                if d == b:
                    nombreMasLargo = f'El nombre con mayor cantidad de caracteres es: {nombre2}'
                    numCaracteres = f'El nombre tiene : {b} caracteres'
                if d == c:
                    nombreMasLargo = f'El nombre con mayor cantidad de caracteres es: {nombre3}'
                    numCaracteres = f'El nombre tiene : {c} caracteres'

        return render_template('ejercicio2.html', nombre1Input=nombre1,nombre2Input=nombre2,nombre3Input=nombre3,nombreMasLargoInput=nombreMasLargo, numCaracteresInput=numCaracteres)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)