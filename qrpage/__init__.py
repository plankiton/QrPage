from flask import Flask, request, render_template as render

qrpage = Flask('qrpage Society')
qrpage.config['SECRET_KEY'] = 'generic_secret_key'

@qrpage.route('/criar_link', methods = ['POST', 'GET'])
def create():
    return render('create.html')

@qrpage.route('/', methods = ['POST', 'GET'])
def index():
    data = request.args.to_dict()
    data['description'] = data['description'] if 'description' in data else None
    data['instagram'] = data['instagram'] if 'instagram' in data else None
    data['whatsapp'] = data['whatsapp'] if 'whatsapp' in data else None
    data['email'] = data['email'] if 'email' in data else None
    data['name'] = data['name'] if 'name' in data else None

    data['instagram_link'] = data['instagram_link'] if 'instagram_link' in data else None
    data['whatsapp_link'] = data['whatsapp_link'] if 'whatsapp_link' in data else None
    data['email_link'] = data['email_link'] if 'email_link' in data else None
    data['name_link'] = data['name_link'] if 'name_link' in data else None

    styles = data['styles'] = data['styles'] if 'styles' in data else '/static/style.css'

    if not data['name']:
        return render('create.html', styles=styles)

    return render('index.html', data=data, styles=styles)
