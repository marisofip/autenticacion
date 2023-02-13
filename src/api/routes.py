"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

api = Blueprint('api', __name__)

@api.route("/token", methods=["POST"])
def create_token():
    email = request.json.get("email", None)
    password = request.json.get("password", None)
    if email != "test" or password != "test":
        return jsonify({"msg": "Bad email or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)


@api.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    if not email:
        return jsonify({"message": "Email is required"}), 400
    if not password:
        return jsonify({"message": "Password is required"}), 400

    foundUser = User.query.filter_by(email=email).first()

    if not foundUser:
        return jsonify({"message": "Email/Password are incorrects"}), 401
    # if not check_password_hash(foundUser.password, password): return jsonify({"message": "Email/Password are incorrects"}), 401
    if not check_password_hash(foundUser.password, password):
        return jsonify({"message": "Email/Password are incorrects"}), 401

    expires = datetime.timedelta(days=3)
    access_token = create_access_token(
        identity=foundUser.id, expires_delta=expires)

    data = {
        "access_token": access_token,
        "user": foundUser.serialize()
    }

    return jsonify(data), 200


@api.route('/register', methods=['POST'])
def register():

    nombre = request.json.get('nombre')
    apellido = request.json.get('apellido')
    rut = request.json.get('rut')
    direccion = request.json.get('direccion')
    comuna = request.json.get('comuna')
    telefono = request.json.get('telefono')
    ciudad = request.json.get("ciudad")
    region = request.json.get("region")
    codigoPostal = request.json.get("codigoPostal")
    email = request.json.get('email')
    password = request.json.get('password')


    if not email:
        return jsonify({"message": "Email is required"}), 400
    if not password:
        return jsonify({"message": "Password is required"}), 400

    foundUser = User.query.filter_by(email=email).first()
    if foundUser:
        return jsonify({"message": "Email already exists"}), 400

    user = User()

    user.email = email
    user.password = generate_password_hash(password)
    user.nombre = nombre
    user.apellido = apellido
    user.telefono = telefono
    user.rut = rut
    user. comuna = comuna
    user.direccion = direccion
    user.codigoPostal = codigoPostal
    user.ciudad = ciudad
    user.region = region

 
    user.save()

    if user:
        expires = datetime.timedelta(days=3)
        access_token = create_access_token(
            identity=user.id, expires_delta=expires)

        data = {
            "access_token": access_token,
            "user": user.serialize()
        }

        return jsonify(data), 201