# Generated by Django 3.0.4 on 2020-04-09 12:03

from django.db import migrations
import modules.core.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks
import wagtailnhsukfrontend.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200409_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('rich_text', wagtail.core.blocks.RichTextBlock(group=' Content')), ('block_quote', wagtail.core.blocks.BlockQuoteBlock(group=' Content')), ('embed', wagtail.embeds.blocks.EmbedBlock(group=' Content')), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))], group=' NHS Components')), ('panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group=' NHS Components')), ('promo', wagtail.core.blocks.StructBlock([('link_page', wagtail.core.blocks.PageChooserBlock(label='Page', required=False)), ('url', wagtail.core.blocks.URLBlock(label='URL', required=False)), ('heading', wagtail.core.blocks.CharBlock(required=True)), ('description', wagtail.core.blocks.CharBlock(required=False)), ('content_image', wagtail.images.blocks.ImageChooserBlock(label='Image', required=False)), ('alt_text', wagtail.core.blocks.CharBlock(required=False)), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2))], group=' NHS Components')), ('expander', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=True)), ('body', wagtail.core.blocks.StreamBlock([('richtext', wagtail.core.blocks.RichTextBlock()), ('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('image', wagtail.core.blocks.StructBlock([('content_image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('alt_text', wagtail.core.blocks.CharBlock(help_text='Only leave this blank if the image is decorative.', required=False)), ('caption', wagtail.core.blocks.CharBlock(required=False))])), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('summary_list', wagtail.core.blocks.StructBlock([('rows', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.SummaryListRowBlock)), ('no_border', wagtail.core.blocks.BooleanBlock(default=False, required=False))]))], required=True))], group=' NHS Components')), ('grey_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(label='heading', required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no heading. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group=' NHS Components')), ('inset_text', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(required=True))], group=' NHS Components')), ('panel_list', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('left_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))])), ('right_panel', wagtail.core.blocks.StructBlock([('label', wagtail.core.blocks.CharBlock(required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Ignore this if there is no label. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('body', wagtail.core.blocks.RichTextBlock(required=True))]))])))], group=' NHS Components')), ('promo_group', wagtail.core.blocks.StructBlock([('column', wagtail.core.blocks.ChoiceBlock(choices=[('one-half', 'One-half'), ('one-third', 'One-third')])), ('size', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Default'), ('small', 'Small')], required=False)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2)), ('promos', wagtail.core.blocks.ListBlock(wagtailnhsukfrontend.blocks.BasePromoBlock))], group=' NHS Components')), ('warning_callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))], group=' NHS Components')), ('table', modules.core.blocks.TableBlock(group=' NHS Components')), ('panel_table', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('table', modules.core.blocks.TableBlock())], group=' NHS Components'))], blank=True, verbose_name='Body blocks'),
        ),
    ]
