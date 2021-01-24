from flask import Flask

from flask_pymongo import PyMongo

from flask import jsonify, request

app =Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/phonebook"


mongo = PyMongo(app)

output = []

// Get all contact
@app.route('/pb', methods=['GET'])
def get_all_data():
   pb = mongo.db.pb
   for q in pb.find():
        output.append({ 'Name' : q['Name'],'Contact': q['Contact'],'Email':q['Email']})

   return jsonify({ "result": output})

    

// Search a contact using Name      
@app.route('/pb/<Name>',methods=['GET'])
def get_one_data(Name):
    pb = mongo.db.pb

    q= pb.find_one({'Name' : Name})

    if q:
      output = { 'Name' : q['Name'],'Contact': q['Contact'],'Email':q['Email']}
    else:
      output="NO record"
    return jsonify({'result': output})    




// Adding a contact
@app.route('/pb',methods=['POST'])
def add_data():
    pb = mongo.db.pb

    Name= request.json['Name']
    Contact=request.json['Contact']
    Email=request.json['Email']
    

   
    data_id=pb.insert({ 'Name' : Name,'Contact': Contact,'Email':Email})
    new_data = pb.find_one({'Name': Name})

    output = { 'Name' : new_data['Name'],'Contact': new_data['Contact'],'Email':new_data['Email']}
    return jsonify({'result': output})




//DELETE a Contact
@app.route('/pb/<Name>',methods=['DELETE'])
def data_user(Name):
     pb = mongo.db.pb
     q= pb.delete_one({'Name': Name})

     output = "Deleted Successfully"

     return jsonify({'result': output})



if __name__ == '__main__':
    app.run(debug=True)

    
