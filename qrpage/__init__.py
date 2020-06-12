from flask import Flask, request, render_template as render

qrpage = Flask('qrpage Society')
qrpage.config['SECRET_KEY'] = 'generic_secret_key'

forms = ('description', 'slogan', 'instagram', 'whatsapp', 'email', 'name',
         'instagram_link', 'whatsapp_link', 'email_link', 'back', 'logo')

@qrpage.route('/criar_link', methods = ['POST', 'GET'])
def create():
    return render('create.html')

@qrpage.route('/', methods = ['POST', 'GET'])
def index():
    data = request.args.to_dict()

    for form in forms:
        data[form] = data[form] if form in data else None

    styles = data['styles'] = data['styles'] if 'styles' in data else '/static/style.css'

    if not data['name']:
        return render('create.html', styles=styles)

    return render('index.html', data=data, styles=styles)
