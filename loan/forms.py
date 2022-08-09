from django import forms


class loaninputs(forms.Form):
    rate = forms.FloatField(label='Loan Rate %',widget=forms.NumberInput(attrs={'class':'form-control-sm'}))
    nper = forms.IntegerField(label='Length of Loan in Months',widget=forms.NumberInput(attrs={'class':'form-control-sm'}))
    pv = forms.FloatField(label='Loan Amount',widget=forms.NumberInput(attrs={'class':'form-control-sm'}))


 