import bottle

app = bottle.Bottle()

form_html = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="/bmi" method='GET'>
<fieldset>
<legend>BMI Calculator</legend>
<ul>
    <li>Weight <input name="weight"></li>
    <li>Heigth <input name="height"></li>
</ul>
<input type="submit" value="Calculate BMI">
</fieldset>
</form>
</body>
<p>{{message}}</p>
</html>

"""




form_bmi = """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="/" method='GET'>
<p>{{message}}</p>
<input type="submit" value="Return">
</html>

"""

@app.route('/')
def root():
    return bottle.template(form_html,message="")

@app.route('/bmi')
def bmicalc():
    bmiresult=""
    if 'weight' in bottle.request.query and 'height' in bottle.request.query:
        bmiresult = "With a weight of " + bottle.request.query['weight'] \
                + " and a height of " + bottle.request.query['height'] \
                    + " your BMI is " \
                        + str(float(bottle.request.query['weight']) / (float(bottle.request.query['height'])**2))
    return bottle.template(form_bmi,message=bmiresult)

if __name__ == "__main__":
    app.run();

