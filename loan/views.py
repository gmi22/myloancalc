import csv
from fileinput import filename
from urllib import response
from django.shortcuts import render
import json
from django.http import HttpResponse
from .forms import loaninputs
from .import views
import numpy as np
import numpy_financial as npf
import pandas as pd
from openpyxl import Workbook
from io import BytesIO

# Create your views here.


def loans(request):

    monthlyPayment = 0
    total_int = 0
    loan_data = []
    tot_pmt = 0


    form = loaninputs
    if request.method == 'POST' and "get_data" in request.POST:
        # create a form instance and populate it with data from the request:
        form = loaninputs(request.POST or None)
        # check whether it's valid:
        if form.is_valid():

            rate = form.cleaned_data['rate']
            nper = form.cleaned_data['nper']
            pv = form.cleaned_data['pv']
            
            

        else:

            form = loaninputs()




        pmt_num = []

        int_list = []

        prnc_list = []

        pmt_list = []

        bal = []

        bal_hold = 0






        for i in range (1,nper+1):
            pmt_num.append(i)
                    

        for i in range(1,nper+1):
            nt_pmt = int_list.append(int((npf.ipmt((rate/12)/100,i,nper,-pv))))
                    

        for i in range(1,nper+1):
            prnc_pmt = prnc_list.append(int((npf.ppmt((rate/12)/100,i,nper,-pv))))
                    
        for i in range(1,nper+1):
            tot_pmt = pmt_list.append(int((npf.pmt((rate/12)/100,nper,-pv))))
                    

        bal_hold=pv-prnc_list[0]

        bal.append(bal_hold)
                    

        for i in range(1,nper):
            bal_hold = bal_hold - prnc_list[i]
                    
            bal.append(bal_hold)

                    

                    
                    
        data = {
                    'Interest':int_list,
                    'Principle':prnc_list,
                    'Payment':pmt_list,
                    'Balance':bal
                }



        df = pd.DataFrame(data,index = pmt_num).style.format("{:,.0f}")

             

        final_df = df.data

        

        final_json = final_df.reset_index().to_json(orient ='records')

        loan_data = []





        loan_data = json.loads(final_json)


        for i in range(0, len(loan_data)):
            loan_data[i]['Interest'] ='{:,}'.format(loan_data[i]['Interest'])
            loan_data[i]['Principle'] ='{:,}'.format(loan_data[i]['Principle'])
            loan_data[i]['Payment'] ='{:,}'.format(loan_data[i]['Payment'])
            loan_data[i]['Balance'] ='{:,}'.format(loan_data[i]['Balance'])

    

        total_int = '{:,}'.format(final_df['Interest'].sum())

        monthlyPayment = '{:,}'.format(round(npf.pmt((rate/12)/100,nper,-pv)),2)


    


        


    return render(request,'loan/loan.html', {'form':form,'result':loan_data,'total_int':total_int,'tot_pmt':monthlyPayment })





        











    




