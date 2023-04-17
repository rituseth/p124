from flask import Flask , request , jsonify 

app = Flask(__name__)

tasks = [
    { 
    'id': 1 , 
    'title' : u'buy electronics',  
    'describtion' : u'tab , phone , laptop ' , 
    'done' : False 
    
     }, 
    { 
    'id': 2 , 
    'title' : u'Learn Python ',  
    'describtion' : u' find good python tutorial ' , 
    'done' : False  
     },
]


@app.route('/add-data' , methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status' : 'error' , 
            'messsge' : 'provide data' , 
            
        } , 400)
        
        
task = {
   
        'id': tasks[-1]['id']+1 , 
        'title' : request.json['title'],  
        'describtion' : request.json.get('describtion' , '') , 
        'done' : False  
        }
tasks.append(task)
return jsonify({
          'status' : 'success' ,
          'message' : 'task added' 
          
               })



@app.route('/get-data')  
def get_task():
    return jasonify({
        'data': tasks 
         
    })

if (__name__ == "__main__"): 
  app2.run(debug=True)

