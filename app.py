from  flask import Flask,render_template


FAI=Flask(__name__)

@FAI.route('/Static_Files')
def Static_Files():
    return render_template('Static_Files.html')


@FAI.route('/NewData')
def Navigate():
    return render_template('Navigate.html')

if __name__=='__main__':
    FAI.run(debug=True)