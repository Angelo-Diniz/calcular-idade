from flask import Flask, request, jsonify, render_template, send_from_directory
import datetime
import time

from flask_swagger_ui import get_swaggerui_blueprint


def swagger_spec():
    spec = {
        'openapi': '3.0.0',
        'info': {
            'title': 'Calcular Idade',
            'version': '1.0.0',
            'description': 'API para calcular a idade com base na data de nascimento'
        },
        'paths': {
            '/calcular_idade': {
                'post': {
                    'summary': 'Calcula a idade com base na data de nascimento',
                    'requestBody': {
                        'required': True,
                        'content': {
                            'application/json': {
                                'schema': {
                                    'type': 'object',
                                    'properties': {
                                        'data_nascimento': {
                                            'type': 'string',
                                            'format': 'date',
                                            'example': '20/04/1990'
                                        }
                                    }
                                }
                            }
                        }
                    },
                    'responses': {
                        '200': {
                            'description': 'Idade calculada com sucesso',
                            'content': {
                                'application/json': {
                                    'schema': {
                                        'type': 'object',
                                        'properties': {
                                            'idade': {
                                                'type': 'integer',
                                                'example': 31
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        '400': {
                            'description': 'Erro de validação',
                            'content': {
                                'application/json': {
                                    'schema': {
                                        'type': 'object',
                                        'properties': {
                                            'erro': {
                                                'type': 'string',
                                                'example': 'Data inválida'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return spec


app = Flask(__name__)

@app.route('/swagger.json')
def swagger():
    return jsonify(swagger_spec())

SWAGGER_URL = '/api/docs'
API_URL = '/swagger.json'

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Calcular Idade'
    }
)

app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manifest.json')
def manifest():
    return send_from_directory('.', 'manifest.json')

@app.route('/service-worker.js')
def service_worker():
    return send_from_directory('.', 'service-worker.js')

@app.route('/imagens/icon.png')
def icon():
    return send_from_directory('.', 'icon.png')

@app.route('/icon-512.png')
def icon_512():
    return send_from_directory('.', 'icon-512.png')

@app.route('/calcular_idade', methods=['POST'])
def calcular_idade():
    start_time = time.time()

    if not request.json or 'data_nascimento' not in request.json:
        return jsonify({"erro": "A data de nascimento não foi enviada"}), 400

    try:
        data_nascimento = datetime.datetime.strptime(request.json['data_nascimento'], '%d/%m/%Y')
    except ValueError:
        return jsonify({"erro": "Data de nascimento inválida"}), 400

    hoje = datetime.datetime.now()

    if data_nascimento > hoje:
        return jsonify({"erro": "A data de nascimento não pode estar no futuro"}), 400

    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    end_time = time.time()

    tempo_execucao_ms = (end_time - start_time) * 1000

    return jsonify({"idade": idade, "tempo_execucao_ms": tempo_execucao_ms})

if __name__ == '__main__':
    app.run(debug=True)
