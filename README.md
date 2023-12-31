# pedramoura-app-backend

## Requirements
### Python modules

Below are the main imported modules:

* ``Flask``: A web framework used to create the application and define routes.
* ``Flask-SQLAlchemy``: A Flask extension for integration with SQLAlchemy databases.
* ``Flask-CORS``: A Flask extension for handling Cross-Origin Resource Sharing (CORS) policies.
* ``firebase_admin``: A library for integration with the Firebase Admin SDK.
* ``functools``: A Python module for functional programming used to create decorators.
* ``json``: A Python module for manipulating data in JSON format.

```bash
pip install flask flask_sqlalchemy flask_cors firebase_admin
```

### Data models

The API defines two data models that correspond to tables in an SQLite database. Here are the data models:

Rota Model
* ``id``: Primary key of the route (integer).
* ``quantidade``: Quantity associated with the route (integer).
* ``dataEntrega``: Delivery date of the route (string).
* ``kms``: Kilometers of the route (integer).
* ``status``: Route status (string).

Pedido Model
* ``id``: Primary key of the order (integer).
* ``idRota``: Foreign key referencing a route (integer).
* ``nomeCliente``: Customer's name (string).
* ``endereco``: Delivery address (string).
* ``observacoes``: Order observations (string).
* ``telefone``: Customer's phone number (string).
* ``itensPedido``: Order items in JSON format (text).
* ``statusEntrega``: Order delivery status (string).
* ``observacoesEntrega``: Delivery observations (string).

## Endpoints
The API defines several routes to perform CRUD (Create, Read, Update, Delete) operations on routes and orders. Below are the main routes:

### Endpoints for Rota

<details>
 <summary><code>POST</code> <code><b>/rotas</b></code> <code>(create new rota)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | None      |  required | object (JSON)           | N/A  |


##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | { "message": "Rota criada com sucesso, ID: X" }                     |


##### JSON object example
```json
{
    "quantidade": 10,
    "dataEntrega": "09/10/2023",
    "kms": 492,
    "status": "EM_PREPARACAO"
}
```

</details>


<details>
 <summary><code>PUT</code> <code><b>/rotas/idRota</b></code> <code>(edit existing rota data)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | idRota    |  required | required | int ($int64) | rota ID                                                           |


##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | { "message": "Rota atualizada com sucesso, ID: X" }                 |
> | `404`         | `application/json`                | { "message": "Rota não encontrada, ID: X" }                         |

</details>


<details>
 <summary><code>GET</code> <code><b>/rotas</b></code> <code>(gets all available rota)</code></summary>

##### Parameters

> None

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | JSON containing all available rota                              |

</details>


<details>
 <summary><code>GET</code> <code><b>/rotas/idRota</b></code> <code>(gets rota by id)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | idRota    |  required | required | int ($int64) | rota ID                                                           |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | JSON containing rota data                                       |
> | `404`         | `application/json`                | { "message": "Rota não encontrada, ID: X" }                         |

</details>


<details>
 <summary><code>DELETE</code> <code><b>/rotas/idRota</b></code> <code>(delete rota by id)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | idRota    |  required | required | int ($int64) | rota ID                                                           |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | { "message": "Rota excluída com sucesso, ID: X" }                   |
> | `404`         | `application/json`                | { "message": "Rota não encontrada, ID: X" }                         |

</details>


### Endpoints for Pedido

<details>
 <summary><code>POST</code> <code><b>/pedidos</b></code> <code>(create new pedido)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | None      |  required | object (JSON)           | N/A  |


##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | { "message": "Pedido criado com sucesso, ID: X" }                   |


##### JSON object example
```json
{
    "idRota": 3,
    "nomeCliente": "Vinicius Keller",
    "endereco": "Av dos Estados 430, Sao Sebastiao do Cai",
    "observacoes": "testes",
    "telefone": "51 997264859",
    "itensPedido": ["5 kg - Contra File", "5 kg - File Mignon"],
    "statusEntrega": "PRONTO_PARA_ENTREGA",
    "observacoesEntrega": "testes"
}
```

</details>


<details>
 <summary><code>PUT</code> <code><b>/pedidos/idPedido</b></code> <code>(edit existing pedido data)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | idPedido  |  required | required | int ($int64) | pedido ID                                                         |


##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | { "message": "Pedido atualizado com sucesso, ID: X" }               |
> | `404`         | `application/json`                | { "message": "Pedido não encontrado, ID: X" }                       |

</details>


<details>
 <summary><code>GET</code> <code><b>/pedidos</b></code> <code>(gets all available pedido)</code></summary>

##### Parameters

> None

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | JSON containing all available pedido                            |

</details>


<details>
 <summary><code>GET</code> <code><b>/pedidos/idPedido</b></code> <code>(gets pedido by id)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | idPedido  |  required | required | int ($int64) | pedido ID                                                         |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | JSON containing pedido data                                     |
> | `404`         | `application/json`                | { "message": "Pedido não encontrado, ID: X" }                       |

</details>


<details>
 <summary><code>DELETE</code> <code><b>/pedidos/idPedido</b></code> <code>(delete pedido by id)</code></summary>

##### Parameters

> | name      |  type     | data type               | description                                                           |
> |-----------|-----------|-------------------------|-----------------------------------------------------------------------|
> | pedidos   |  required | required | int ($int64) | pedido ID                                                         |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`                | { "message": "Pedido excluído com sucesso, ID: X" }                 |
> | `404`         | `application/json`                | { "message": "Pedido não encontrado, ID: X" }                       |

</details> 

### Firebase Credentials

Replace the path ```credentials/firebase-credentials.json``` with the actual path to your Firebase service credentials.

### Cloning the repository
```bash
git clone https://github.com/marcelozilio/pedramoura-delivery-route
```

## Usage
### Running web service
```bash
cd pedramoura-app-backend
python main.py
```
The output must show the IP address:
```console
 * Serving Flask app 'main'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 816-201-332

```