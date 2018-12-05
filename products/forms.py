from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = [
			'title',
			'description',
			'price',
			'summary',

		]


class RawProductForm(forms.Form):
	"""docstring for RawProductForm"""
	title		= forms.CharField(label='Your Title' ,widget=forms.TextInput(
												attrs={
												'class':'my-class',
												'placeholder':'Enter title here'
												}
											)
								)
	description	= forms.CharField(widget=forms.Textarea(
									attrs={
											"rows": 20,
											"cols": 50,
											"class":"my-class" 
										}
									)
								)
	price		= forms.DecimalField(initial=199.9)
