<h2>Presto Challenge</h2>

There are two solutions to the challenge:
- Python - `python_solution` directory
- Node   - `node_solution` directory

<h3>Python</h3>

The main script lies in `python_solution/1uphealth_challenge.py`. Please follow the following steps to run the script:
1. Install dependencies:
```
# Make sure python is installed in the system.

# Create virtual env
$ cd python_solution
$ python -m venv venv
$ source venv/bin/activate

# Install python dependencies
$ pip install -r requirements.txt

```
2. Execute the script:
```
$ python 1uphealth_challenge.py {firstname} {lastname}
```

The sql query can be found at: `python_solution/sql/allergyinfo.sql`.

<h3>Node Solution</h3>

The script for nodejs solution can be found in `node_solution/1uphealth_challenge.js`.

Follow the following steps to run the script:
1. Install dependencies:
```
$ cd node_solution
$ npm install
```
2. Execute the script:
```
$ node ./1uphealth_challenge.js {firstname} {lastname}
```

You can find the sql query at: `node_solution/queries/allergyinfo.sql`. 
