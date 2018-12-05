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
												'placeholder':'Enter title here (new keyword is required)'
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


	def clean_title(self,*args,**kwargs):
		title = self.cleaned_data.get("title")
		if not "new" in title:
			raise forms.ValidationError("This is not a valid title")
		return title 