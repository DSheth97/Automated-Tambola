from flask import Flask,render_template,url_for,request,redirect,make_response
from flask_sqlalchemy import SQLAlchemy
from random import randint
from flask_wtf import FlaskForm
from wtforms import StringField, FormField, FieldList, HiddenField, IntegerField
from random import sample
import numpy
import pdfkit

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///housie.db'
app.config['SECRET_KEY'] = 'secret'
db = SQLAlchemy(app)

board=[]

#Functions

def GenerateTicket():
    from random import randint
    from random import sample
    import numpy
    arr=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
    ctr=[0,0,0,0,0,0,0,0,0]
    
    seq1=[i for i in range(1,9)]
    seq2=[i for i in range(10,19)]
    seq3=[i for i in range(20,29)]
    seq4=[i for i in range(30,39)]
    seq5=[i for i in range(40,49)]
    seq6=[i for i in range(50,59)]
    seq7=[i for i in range(60,69)]
    seq8=[i for i in range(70,79)]
    seq9=[i for i in range(80,90)]

    for i in range(3):
        for j in range(9):
            if(j==0):
                arr[i][j] = sample(seq1,k=1)[0]
                seq1.remove(arr[i][j])
            elif(j==1):
                arr[i][j] = sample(seq2,k=1)[0]
                seq2.remove(arr[i][j])
            elif(j==2):
                arr[i][j] = sample(seq3,k=1)[0]
                seq3.remove(arr[i][j])
            elif(j==3):
                arr[i][j] = sample(seq4,k=1)[0]
                seq4.remove(arr[i][j])
            elif(j==4):
                arr[i][j] = sample(seq5,k=1)[0]
                seq5.remove(arr[i][j])
            elif(j==5):
                arr[i][j] = sample(seq6,k=1)[0]
                seq6.remove(arr[i][j])
            elif(j==6):
                arr[i][j] = sample(seq7,k=1)[0]
                seq7.remove(arr[i][j])
            elif(j==7):
                arr[i][j] = sample(seq8,k=1)[0]
                seq8.remove(arr[i][j])
            elif(j==8):
                arr[i][j] = sample(seq9,k=1)[0]
                seq9.remove(arr[i][j])
            else:
                print("Error generating ticket") 
    #showTicket(arr)
    lst=numpy.transpose(arr)
    #print(lst)
    for j in range(9):
        lst[j].sort()
        
    #print(lst)
    tkt = numpy.transpose(lst)
    
    for i in range(3):
        removeSeq=[z for z in range(9)]
        j=0
        while(j<=3):
            if((i==2) and (0 in ctr)):      #To not have 3 numbers in single column
                s = ctr.index(0)
                removeSeq.remove(s)
            else:
                s=sample(removeSeq,k=1)[0]
                removeSeq.remove(s)
            
            if(ctr[s]<2):
                tkt[i][s]=0
                ctr[s]+=1
            else:
                j=j-1
            j=j+1
    #showTicket(tkt)
    return tkt

def showTicket(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if(arr[i][j]!=0):
                print(arr[i][j],end="\t")
            else:
                print(" ",end="\t")
        print()

def convert2string(arr):
    tkt=""
    for row in arr:
        for item in row:
            tkt=tkt+" "+str(item)
    return tkt.strip()

def GenerateRandomButton(board):
  
    k=randint(1,90)
    if(k not in board):
        return k
    else:
        return GenerateRandomButton(board)

#DB Models

class Player(db.Model):
    player_id = db.Column(db.Integer, primary_key = True,  autoincrement=True)
    name = db.Column(db.String(50),nullable = False)
    contact = db.Column(db.String(10),nullable = False)
    tickets = db.relationship('Ticket', backref='player', lazy=True)

    def __repr__(self):
        return '<Player %r>' % self.name

class Ticket(db.Model):
    pid = db.Column(db.Integer,db.ForeignKey('player.player_id'), nullable=False)
    ticket_id = db.Column(db.Integer, primary_key = True,  autoincrement=True)
    ticket = db.Column(db.String(100),nullable=False)
    winner = db.relationship('Winner', backref='winner', lazy=True)
    
class Prizes(db.Model):
    prize_id = db.Column(db.Integer,primary_key=True)
    beautyspot = db.Column(db.JSON)
    temperature = db.Column(db.JSON)
    early5 = db.Column(db.JSON)
    early7 = db.Column(db.JSON)
    early9 = db.Column(db.JSON)
    corners4 = db.Column(db.JSON)
    corners6 = db.Column(db.JSON)
    sandwich = db.Column(db.JSON)
    firstline = db.Column(db.JSON)
    middleline = db.Column(db.JSON)
    lastline = db.Column(db.JSON)
    loveline = db.Column(db.JSON)
    breakfast = db.Column(db.JSON)
    lunch = db.Column(db.JSON)
    dinner = db.Column(db.JSON)
    fullhouse = db.Column(db.JSON)

class Winner(db.Model):
    pid = db.Column(db.Integer,db.ForeignKey('player.player_id'), nullable=False)
    tid = db.Column(db.Integer,db.ForeignKey('ticket.ticket_id'), primary_key=True)
    prize = db.Column(db.String(100),nullable=False)
    amount = db.Column(db.Integer)


#Flask Forms

class FullHouseEntryForm(FlaskForm):
    id = IntegerField()

class FullHousesForm(FlaskForm):
    amounts = FieldList(FormField(FullHouseEntryForm),min_entries=0)







#Routes 

@app.route('/',methods=['GET','POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form['submit'] == 'GenerateNumber':
            newnum = GenerateRandomButton(board)
            board.append(newnum)
            return  redirect(url_for('index'))
            #render_template('index.html',board=board,len=len(board))
    else:
        #board.clear()
        playerList = Player.query.join(Ticket).add_columns(Player.player_id,Player.name,Ticket.ticket_id)

        mapp=dict()

        for i in playerList:
                    
            print(i[1],i[2],i[3])
            if i[2] in mapp:
                mapp[i[2]].append(str(i[3]))
            else:
                mapp[i[2]]=[str(i[3])]

        print(mapp)  
    return render_template('index.html',board=board,len=len(board),players=mapp)


@app.route('/gen',methods=['POST','GET'])
def genTickets():
    if request.method=="POST":
        totalTickets = int(request.form['tickets'])
        name = request.form['name']
        contact = request.form['contact']
        arr=[]
        for i in range(totalTickets):
            arr.append(GenerateTicket())
        new_player = Player(name=name,contact=contact)
        try:
            db.session.add(new_player)
            db.session.commit()
            print("Player commited")
            for j in range(totalTickets):
                tkt=convert2string(arr[j]) 
                print("Converted tkt", tkt) 
                print("Player id = ",new_player.player_id)  
                new_ticket = Ticket(pid = new_player.player_id, ticket = tkt)
                db.session.add(new_ticket)
                db.session.commit()
                print("Ticket committed")
        except:
            return "Error generating player"
        
        return redirect('/show/'+str(new_player.player_id))
    else:
        return render_template('tickets.html')

@app.route('/show/<int:pid>',methods=['POST','GET'])
def display(pid):
    if request.method=="POST":
        if(request.form['submitbtn'])=='Back':
            return redirect(url_for('genTickets'))
        else:
            imgkit.from_url('/show/'+str(pid), 'out.jpg')
    else:
        #share('/show/'+str(pid))
        rendered = render_template('showTickets.html',tkts=Ticket.query.filter_by(pid=pid).all())
        config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
        pdf = pdfkit.from_string(rendered,False,configuration=config)

        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=output.pdf'

        return response


@app.route('/allotPrizes',methods=['GET','POST'])
def allotPrizes():
    form = FullHousesForm()
    print(request.method)
    if request.method == 'POST':
        if(request.form['AddFullHouse']=='+'):
            amt = request.form['FullHouse']
            print(amt)
            form.amounts.append_entry(80)
            print(form.amounts)
            return render_template('allotPrizes.html',form=form)
        else:
            print("Button not pressed")
    #fhs = [{1:80},{2:60}]
    #form = FullHousesForm()
    #form.amounts.append_entry(fhs)   
    else:
        return render_template('allotPrizes.html',form=form)

if(__name__=='__main__'):
    app.run(debug=True)
