from django import forms

class submitRecharge(forms.Form):
	ip=forms.CharField(
		required=False,
		label='',
		widget=forms.TextInput(
		attrs={
			"placeholder":"Enter the ID",}
		)
		)
	money=forms.IntegerField(
		required=False,
		label='',
		widget=forms.TextInput(
			attrs={
			"placeholder":"Enter the money",
			}
			)
		)


	
class regForm(forms.Form):
	username=forms.CharField(
		required=False,
		label='',
		widget=forms.TextInput(
			attrs={
			"placeholder":"username"
			}))
	password=forms.CharField(
		required=False,
		label='',
		widget=forms.TextInput(
			attrs={
			"placeholder":"username"
			}))
	add=forms.CharField(
		required=False,
		label='',
		widget=forms.TextInput(
			attrs={
			"placeholder":"username"
			}))

class loginForm(forms.Form):
	username=forms.CharField(
		required=False,
		label='',
		widget=forms.TextInput(
			attrs={
			"placeholder":'username',
			}))
	password=forms.CharField(
		required=False,
		label='',
		widget=forms.TextInput(
			attrs={
			"placeholder":'password',
			}))