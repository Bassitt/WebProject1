from flask import Flask
# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)
app.config["DEBUG"] = True
# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

@app.route('/')
@app.route('/exer')
def exer():
    return '''
<html>
  <head>
    <title>Title of the Document</title>
  </head>
  <body>
  
    <script>
var max = 100
var min = 0
var a = Math.floor(Math.random() * (max - min + 1)) + min;
var b = Math.floor(Math.random() * (max - min + 1)) + min;
var z = a + b 
"<br>"
document.write("a = ", a + "<br>")
document.write(" b = ", b + "<br>")
document.write("a + b =")
      function getInputValue() {
        // Selecting the input element and get its value 
        let inputVal = document.getElementsByClassName("inputClass")[0].value;
        // Displaying the value
        document.write("a = ", a + "<br>")
document.write(" b = ", b + "<br>")
document.write("a + b =")
if (inputVal == z ) {
   document.write ( inputVal+ " Your answer" +" is correct"+"<br>")
} else {
   document.write( inputVal+ " answer"+ " is not correct" + "<br>")
}
      }
    </script>
 <input type="text" placeholder="Enter Answer " id="inputId" class="inputClass">
    <button type="button" onclick="getInputValue();">Check</button>
  </body></html>
  '''
if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)
