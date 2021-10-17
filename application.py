from flask import Flask, render_template, request, url_for 

app = Flask(__name__) 
 
@app.route("/", methods=["GET"] )
def Datos_personales():
    return render_template("index.html")
 

@app.route("/", methods=["GET","POST"])
def hola():
    #Prensentacion y datos
    name = request.form.get("name")
    apellidos = request.form.get("apellidos")
    dni = request.form.get("dni")
    presentacion = request.form.get("presentacion")
    #Formas de contacto
    email = request.form.get("email")
    nmr = request.form.get("nmr")
    cod_pos = request.form.get("cod_pos")
    fb = request.form.get("fb")
    ig = request.form.get("ig")
    twt = request.form.get("twt")
    #Habilidades
    skill1 = request.form.get("skill1")
    skill2 = request.form.get("skill2")
    skill3 = request.form.get("skill3")
    skill4 = request.form.get("skill4")
    skill5 = request.form.get("skill5")
    #Experiencia laborale
    work1 = request.form.get("work1")
    work2 = request.form.get("work2")
    work3 = request.form.get("work3")
    #Experiencias laborales
    workexp1_1 = request.form.get("workexp1-1")
    workexp1_2 = request.form.get("workexp1-2")
    workexp1_3 = request.form.get("workexp1-3")
    workexp2_1 = request.form.get("workexp2-1")
    workexp2_2 = request.form.get("workexp2-2")
    workexp2_3 = request.form.get("workexp2-3")
    workexp3_1 = request.form.get("workexp3-1")
    workexp3_2 = request.form.get("workexp3-2")
    workexp3_3 = request.form.get("workexp3-3")

    #Estudios 
    sec = request.form.get("sec")
    sup = request.form.get("sup")
    mstr = request.form.get("mstr")
    doc = request.form.get("doc")
    #Hobbies
    hobbie1 = request.form.get("hobbie1")
    hobbie2 = request.form.get("hobbie2")
    hobbie3 = request.form.get("hobbie3")
    hobbie4 = request.form.get("hobbie4")
    
    return render_template("hola.html",name=name,apellidos=apellidos,dni=dni, presentacion=presentacion,
    email=email, nmr=nmr, cod_pos=cod_pos, fb=fb, ig=ig, twt=twt, skill1=skill1, skill2=skill2, skill3=skill3,
    skill4=skill4, skill5=skill5, workexp1=work1, work2=work2, work3=work3,workexp1_1=workexp1_1,workexp1_2=workexp1_2,
    workexp1_3=workexp1_3,workexp2_1=workexp2_1,workexp2_2=workexp2_2, workexp2_3=workexp2_3,workexp3_1=workexp3_1,
    workexp3_2=workexp3_2, workexp3_3=workexp3_3, sec=sec, sup=sup, mstr=mstr, doc=doc, hobbie1=hobbie1,
     hobbie2=hobbie2,hobbie3=hobbie3, hobbie4=hobbie4)
    