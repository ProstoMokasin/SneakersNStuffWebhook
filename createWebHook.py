from dhooks import Webhook, File, Embed

print('webhook bot is alive')

def CreateWebHook(name, sizes, price):
	webhook = Webhook("WEBHOOK_URL")

	embed = Embed(
		description='A new thing is out! :wink:',
		timestamp='now'
		)

	#Making a Discord Webhook
	embed.set_author(name=name, icon_url="https://pmcfootwearnews.files.wordpress.com/2016/12/sns-logo-black_1024x1024.jpg")
	embed.add_field(name='**Sizes**', value='[S](https://www.sneakersnstuff.com/en/product/40044/adidas-pleckgate-tp),'
											' [M](https://www.sneakersnstuff.com/en/product/40044/adidas-pleckgate-tp),'
											' [L](https://www.sneakersnstuff.com/en/product/40044/adidas-pleckgate-tp),'
											' [XL](https://www.sneakersnstuff.com/en/product/40044/adidas-pleckgate-tp)')
	#embed.set_thumbnail("./product.png")
	webhook.send(embed=embed)
	print('webhook sent')
	pass