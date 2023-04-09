from flask import Flask, request, render_template_string

def hello_world(request):
    if request.method == 'POST':
        vals = request.form.getlist('numbers')
        A = float(vals[0])
        B = float(vals[1])
        C = float(vals[2])
        result = (A+B+C)
    else:
        A = ''
        B = ''
        C = ''
        result = ''
    return render_template_string('''
<html
<body style="background-color:greenyellow;">    
<b>Calculator App to sum 3 numbers </b> .<br>
<p>Powered by - <a> Cloud Function </a></p>
<form  method="POST">
    Please input 3 numbers - A,B,C:
    <p>Number A: <input type="text" size = "6" name="numbers" value="{{ v_A }}"></p>
    <p>Number B: <input type="text" size = "6" name="numbers" value="{{ v_B }}"></p>
    <p>Number C: <input type="text" size = "6" name="numbers" value="{{ v_C }}"></p>
    <input type="submit" value="Click here to compute">
    <p>Result: <input type="text" size = "6" name="result" value="{{ v_result }}"></p>
</form>
</html>
''', v_A=A, v_B=B, v_C=C, v_result=result)
