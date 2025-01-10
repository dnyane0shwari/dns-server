from flask import Flask, request, jsonify, render_template

import dns.resolver

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Server logs UI

@app.route('/client')
def client_ui():
    return render_template('client.html')  # NEW: Client UI

@app.route('/resolve', methods=['POST'])
def resolve_domain():
    try:
        domain_name = request.form['domain']
        answers = dns.resolver.resolve(domain_name, 'A')
        ip_addresses = [answer.address for answer in answers]
        return jsonify({'status': 'success', 'ip_addresses': ip_addresses})
    except dns.resolver.NXDOMAIN:
        return jsonify({'status': 'error', 'message': 'Invalid domain name'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
