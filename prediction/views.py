from django.shortcuts import render
import pandas as pd
import joblib
from prediction.forms import ApprovalsForm

reloadModel=joblib.load("C:\\Users\\Krishna P\\ML_Django\\loan.pkl")


def index(request):
    return render(request,'index.html')

def make_appointment(request):
    return render(request,'make_appointment.html')

def mpg(request):
    return render(request,'mpg.html')
def milage_prediction(request):
    if request.method == 'POST':

        temp={}
        temp['cylinders']=int(request.POST['cylinders'])
        temp['displacement']=int(request.POST['displacement'])
        temp['horsepower']=int(request.POST['horsepower'])
        temp['weight']=int(request.POST['weight'])
        temp['acceleration']=int(request.POST['acceleration'])
        temp['model year']=int(request.POST['model_year'])
        temp['origin']=int(request.POST['origin'])
    testData=pd.DataFrame({'x':temp}).transpose()
    scoreval=reloadModel.predict(testData)[0]
    context={'scoreval':scoreval}
    return render(request,'milage_prediction.html',context)

def loan_prediction(request):
    form=ApprovalsForm()
    return render(request,'loan_prediction.html',{'forms':form})

def loan_predicted(request):
    if request.method == 'POST':
        form=ApprovalsForm(request.POST)

        if form.is_valid():
            form.save()
            temp={}
            print("Validation success")
            temp['Gender']=form.cleaned_data['gender']
            temp['Married']=form.cleaned_data['married']
            temp['Dependents']=form.cleaned_data['dependants']
            temp['Education']=form.cleaned_data['graduatededucation']
            temp['Self_Employed']=form.cleaned_data['selfemployed']
            temp['ApplicantIncome']=form.cleaned_data['applicantincome']
            temp['CoapplicantIncome']=form.cleaned_data['coapplicantincome']
            temp['LoanAmount']=form.cleaned_data['loanamount']
            temp['Loan_Amount_Term']=form.cleaned_data['loanamountterm']
            temp['Credit_History']=form.cleaned_data['Credit_History']
            temp['Property_Area']=form.cleaned_data['area']

            testData=pd.DataFrame({'x':temp}).transpose()
            scoreval=reloadModel.predict(testData)[0]
            if scoreval == 1:
                status="There is a High chance that Loan will be Approved"
            else:
                status="I Think Loan will not be Approved. Better Luck!"


    return render(request,'loan_predicted.html',{'val':status})
