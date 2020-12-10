from django import forms




class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class InsertForm(forms.Form):
    TeamNameform = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    PlayerNameform = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    CoachNameform = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    ManagerNameform = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class UpdateForm(forms.Form):

    scoreAform = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    scoreBform = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
   