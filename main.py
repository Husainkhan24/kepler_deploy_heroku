import numpy as np
from flask import *
import pickle
#import requirements.txt

app= Flask(__name__)
model=pickle.load(open('model_DT.pkl','rb'))


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict",methods=['POST'])
def data_pre():
#____________________________________________________________________________
    #list1=[float(i) for i in request.form.values()]
  #  list2=[np.array(list1)]
    #ypred=model.predict(list2)

    #result=''
   # for i in ypred:
   #     if i==1:
    #        result=result+'CONFIRMED'
     #   elif i==2:
      #      result=result+'CANDIDATE'
       # elif i==3:
       #     result=result+'FALSE POSITIVE'
    #return render_template('index.html',print_result='koi_disposition :'.format(result))  
   # return render_template('index.html',print_result="gand me danda")
#_________________________________________________________________________________________     
 
    var1=request.form['koi_score']
    var2=request.form['koi_fpflag_nt']
    var3=request.form['koi_fpflag_ss']
    var4=request.form['koi_fpflag_co']
    var5=request.form['koi_fpflag_ec']
    var6=request.form['koi_period']
    var7=request.form['koi_time0bk']
    var8=request.form['koi_impact']
    var9=request.form['koi_duration']
    var10=request.form['koi_depth']
    var11=request.form['koi_prad']
    var12=request.form['koi_teq']
    var13=request.form['koi_insol']
    var14=request.form['koi_model_snr']
    var15=request.form['koi_tce_plnt_num']
    var16=request.form['koi_steff']
    var17=request.form['koi_slogg']
    var18=request.form['koi_srad']
    var19=request.form['ra']
    var20=request.form['dec']
    var21=request.form['koi_kepmag']
    list1=[var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,var18,var19,var20,var21]
    list2=[np.array(list1)]
    
    ypred=model.predict(list2)    
    result=''
    for i in ypred:
        if i==1:
          result=result+'CONFIRMED'
        elif i==2:
           result=result+'CANDIDATE'
        elif i==3:
            result=result+'FALSE POSITIVE'

    return render_template('res.html',print_result='koi_disposition =='+' '+result)
    
if __name__=='__main__':
    app.run(debug=True)