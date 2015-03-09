from flask import Flask,request,Response,make_response;
from wand.image import Image;

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def convert_svg2png():
  if request.method=='POST':
    try:
      with Image(blob=str(request.form['svg']), format='svg') as image:
        image.read();
        png_image = image.make_blob('png32');
      response = make_response(png_image)
      response.headers['Content-Type'] = 'image/png'
      return response;
    except Exception as e:
      return Response(response=str(e), status=400);
  return '''
      <html><body><form action='/' method='POST'><textarea name=svg></textarea><input type='submit'></form></body></html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080);
