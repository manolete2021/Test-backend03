from email.policy import default
from sre_parse import SUCCESS
from flask import Flask, request, jsonify 
from flask_cors import CORS
from resgister import (
    register_user,
    search_users_id,
    get_all_registers,
    update_user,
    delete_name
)

app=Flask(__name__)
CORS(app)

@app.route("/api/register", methods = ["POST"])
def create_register():
    try:
        data = request.get_json() or {}
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        #validacion requerida en los dos lados backend and frontend, puede ser un solo lado
        if not name or not email or not password:
            return jsonify({"error": "name,email,password son requridos"}), 400

        #registrar usuarios
        sucess_user= register_user(name, email, password)
        if not sucess_user:
            return jsonify ({"error":"no se pudo registrar"}), 400
        
        #retornar usuario creado
        
        return jsonify ({"mensaje" : "usuario registrado exitosamente"}), 201

    except Exception as e:
        return jsonify({"error" : str(e)}), 500

@app.route("/api/registers", methods = ["GET"])
def get_all_registers_endpoint():
    try:
        registros = get_all_registers()
        
        # Convertir las tuplas a diccionarios para JSON
        registros_list = []
        for registro in registros:
            registros_list.append({
                "id": registro[0],
                "name": registro[1],
                "email": registro[2],
                "password": registro[3]
            })
        
        return jsonify({
            "mensaje": "Registros obtenidos exitosamente",
             "respuesta": registros_list
        }), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/registers/<int:id>", methods = ["GET"])
def get_register_by_id(id):
    try:
        usuario = search_users_id(id)
        if usuario is None:
            return jsonify({"error": "usuario no encontrado"}), 404
        
        return jsonify({
            "mensaje": "Usuario obtenido exitosamente",
            "respuesta": {
                "id": usuario[0],
                "name": usuario[1],
                "email": usuario[2],
                "password": usuario[3]
            }
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/registers/<int:id>", methods = ["PUT"])
def update_register(id):
    try:
        data = request.get_json() or {}
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return jsonify({"error": "name, email, password son requeridos"}), 400

        success = update_user(id, name, email, password)
        if not success:
            return jsonify({"error": "no se pudo actualizar el usuario"}), 400
        
        return jsonify({"mensaje": "usuario actualizado exitosamente"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/registers/<int:id>", methods = ["DELETE"])
def delete_register(id):
    try:
        success = delete_name(id)
        if not success:
            return jsonify({"error": "no se pudo eliminar el usuario"}), 400
        
        return jsonify({"mensaje": "usuario eliminado exitosamente"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == "__main__":
    print("iniciando servidor")

    app.run(debug = True, host="0.0.0.0", port=5000)

    



         