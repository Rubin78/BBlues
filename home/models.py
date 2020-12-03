from django.db import models
from wagtail.admin import blocks
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField

from wagtail.core.models import Page
from wagtail.images.blocks import ImageChooserBlock

from home.blocks import CarouselBlock, ProductBlock, CategoriesBlock, BlogBlock, InstagramBlock, IndexcarouselBlock, \
    LookbookBlock, CtaBlock, ListingBlock, PartnerBlock, BlogcardBlock, ComingsoonBlock, SigninBlock, \
    ProductscrollBlock, InfoBlock, BannerBlock, IndexcategoriesBlock, IndexminimalcategoriesBlock, PostheroBlock, \
    InterpostBlock, NumbersBlock, TextBlock, HerolistingmasonaryBlock, ProductlistingmasonaryBlock, \
    Carouseltransition2Block, IndexmoderntitleBlock, ProductindexmodernBlock, Cta2Block, SeperatorBlock, Lookbook2Block, \
    Cta3Block, Instagram2Block, PromoproductBlock, ProductclassicBlock, ProductmodernBlock, BlogproducttextBlock, \
    Cta4Block, ProductmasonaryBlock


class HomePage(Page):
    body=StreamField([
        ('carousel', CarouselBlock()),
        ('product', ProductBlock()),
        ('categories', CategoriesBlock()),
        ('blog', BlogBlock()),
        ('instagram', InstagramBlock()),
        ('indexcarousel', IndexcarouselBlock()),
        ('listing', ListingBlock()),
        ('lookbook', LookbookBlock()),
        ('cta', CtaBlock()),
        ('partner', PartnerBlock()),
        ('blogcard', BlogcardBlock()),
        ('comingsoon', ComingsoonBlock()),
        ('signin', SigninBlock()),
        ('productscroll', ProductscrollBlock()),
        ('info', InfoBlock()),
        ('banner', BannerBlock()),
        ('indexcategories', IndexcategoriesBlock()),
        ('indexminimalcategories', IndexminimalcategoriesBlock()),
        ('posthero', PostheroBlock()),
        ('interpost', InterpostBlock()),
        ('numbers', NumbersBlock()),
        ('text', TextBlock()),
        ('herolistingmasonary', HerolistingmasonaryBlock()),
        ('productlistingmasonary', ProductlistingmasonaryBlock()),
        ('carouseltransition2', Carouseltransition2Block()),
        ('indexmoderntitle', IndexmoderntitleBlock()),
        ('Productindexmodern', ProductindexmodernBlock()),
        ('cta2', Cta2Block()),
        ('seperator', SeperatorBlock()),
        ('lookbook2', Lookbook2Block()),
        ('cta3', Cta3Block()),
        ('instagram2', Instagram2Block()),
        ('promoproduct', PromoproductBlock()),
        ('productclassic', ProductclassicBlock()),
        ('productmodern', ProductmodernBlock()),
        ('blogproducttext', BlogproducttextBlock()),
        ('cta4', Cta4Block()),
        ('productmasonary', ProductmasonaryBlock()),



    ])

    content_panels=Page.content_panels+[
        StreamFieldPanel('body'),
    ]
